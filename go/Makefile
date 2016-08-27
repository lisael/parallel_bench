include ../Makefile.in

GOPATH=$(shell readlink -f .)

all: title bench-montecarlo

title:
	@echo "## Go"
	@echo


bench-%: $*
	@echo "### $*"
	@echo
	@echo "#### Version"
	@echo
	go version | cut -d" "  -f3-
	@echo
	@echo "#### Build"
	@echo
	@echo "\`\`\`"
	$(TIME) go build $*
	@echo
	@echo "#### Executable size"
	@echo
	@du -0 -k $* | cut -f1
	@echo
	@echo "#### Run"
	@echo
	@echo "\`\`\`"
	$(TIME) ./$*
	@echo
