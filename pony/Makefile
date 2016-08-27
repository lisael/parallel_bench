include ../Makefile.in

all: title bench-montecarlo

title:
	@echo "## Pony"
	@echo

bench-%: $*
	@echo "### $*"
	@echo
	@echo "#### Version"
	@echo
	ponyc -v
	@echo
	@echo "#### Build"
	@echo
	@echo "\`\`\`"
	$(TIME) ponyc -o build $*
	@echo
	@echo "#### Executable size"
	@echo
	@du -0 -k build/$* | cut -f1
	@echo
	@echo "#### Run"
	@echo
	@echo "\`\`\`"
	$(TIME) build/$*
	@echo
