#! /usr/bin/python

from cStringIO import StringIO

FIELDS = ["name",
          "lang",
          "run_time",
          "run_mem",
          "build_time",
          "build_mem",
          "exe_size",
          "version",
          ]

HUMAN_FIELDS = {
    "name": "Bench",
    "lang": "Language",
    "run_time": "Duration (s)",
    "run_mem": "Max memory (Kb)",
    "build_time": "Build Duration",
    "build_mem": "Build Max Memory",
    "exe_size": "Executable Size (Kb)",
    "version": "compiler version"
}


class BackIterator(object):
    def __init__(self, it):
        self.cursor = -1
        self.lst = list(it)

    def __next__(self):
        self.cursor += 1
        if self.cursor >= len(self.lst):
            raise StopIteration
        return self.lst[self.cursor]

    def __iter__(self):
        while 1:
            n = self.__next__()
            yield n

    def backup(self):
        self.cursor -= 1
        self.cursor = max(self.cursor, -1)

    def remains(self):
        return self.lst[self.cursor:]


class Bench(object):
    def __init__(self, name, lang):
        self.lang = lang
        self.name = name

    def first_non_empty(self, lines):
        for line in lines:
            if line.strip():
                return line.strip()
            if line.startswith("#"):
                break

    def pass_n_lines_startswith(self, n, sw, lines):
        for line in lines:
            if line.startswith(sw):
                if n == 1:
                    return
                else:
                    return self.pass_n_lines_startswith(n-1, sw, lines)

    def parse_build(self, lines):
        self.pass_n_lines_startswith(2, "```", lines)
        self.pass_n_lines_startswith(2, "|", lines)
        l = lines.__next__()
        _, _, time, mem, _ = [i.strip() for i in l.split("|")]
        return time, mem

    def parse_run(self, lines):
        self.pass_n_lines_startswith(2, "```", lines)
        self.pass_n_lines_startswith(2, "|", lines)
        l = lines.__next__()
        _, _, time, mem, _ = [i.strip() for i in l.split("|")]
        return time, mem

    def parse(self, lines):
        for line in lines:
            if not line.strip():
                continue
            elif line == "#### Version\n":
                self.version = self.first_non_empty(lines)
            elif line == "#### Build\n":
                self.build_time, self.build_mem = self.parse_build(lines)
            elif line == "#### Executable size\n":
                self.exe_size = self.first_non_empty(lines)
            elif line == "#### Run\n":
                self.run_time, self.run_mem = self.parse_run(lines)
            elif line.startswith("### ") or line.startswith("## "):
                lines.backup()
                return

    def as_dict(self):
        result = {}
        for att in FIELDS:
            result[att] = getattr(self, att, "n/a")
        return result


class Language(object):
    def __init__(self, name):
        self.name = name
        self.benchs = []

    def parse(self, lines):
        for line in lines:
            if line.startswith("### "):
                b = Bench(line[4:].strip(), self.name)
                self.benchs.append(b)
                b.parse(lines)
            elif line.startswith("## "):
                lines.backup()
                return

    def bench(self, name):
        for b in self.benchs:
            if b.name == name:
                return b

    def as_dict(self):
        return {r.name: r.as_dict() for r in self.benchs}


class Results(object):
    def __init__(self):
        self.results = []

    def parse(self, lines):
        for line in lines:
            if line.startswith("## "):
                language = Language(line[3:].strip())
                self.results.append(language)
                language.parse(lines)

    def as_dict(self):
        return {r.name: r.as_dict() for r in self.results}


def parse_report():
    with open("report.md") as f:
        return parse_lines(f)


def parse_lines(lines):
    r = Results()
    lines = BackIterator(lines)
    r.parse(lines)
    return r


class Formatter(object):
    def __init__(self, results):
        self.results = []
        for lang in results.values():
            for bench in lang.values():
                self.results.append(bench)
        self.names = {r["name"] for r in self.results}
        self.languages = {r["lang"] for r in self.results}

    def md_rows(self, rows, out):
        for row in rows:
            out.write("| ")
            out.write(" | ".join([row[k] for k in FIELDS]))
            out.write(" |\n")

    def md_table(self, group_by="bench"):
        out = StringIO()
        out.write("| ")
        out.write(" | ".join([HUMAN_FIELDS[k] for k in FIELDS]))
        out.write(" |\n")
        out.write("| ")
        out.write(" | ".join(["---" for k in FIELDS]))
        out.write(" |\n")
        if group_by == "bench":
            for name in self.names:
                results = [r for r in self.results if r["name"] == name]
                self.md_rows(results, out)
        else:
            self.md_rows(self.results, out)
        return out


if __name__ == "__main__":
    results = parse_report().as_dict()
    out = Formatter(results).md_table()
    print out.getvalue()
