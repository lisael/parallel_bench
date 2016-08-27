include ../Makefile.in

all: title bench-montecarlo

title:
	@echo "## Elixir"
	@echo

bench-%: $*
	-rm -rf $*/_build
	@echo "### $*"
	@echo
	@echo "#### Version"
	@echo
	elixir -v | grep -v "^$$" | sed 'N;s/\n/ - /'
	@echo
	@echo "#### Build"
	@echo
	@echo "\`\`\`"
	cd $*; export MIX_ENV=prod; $(TIME) mix escript.build
	@echo
	@echo "#### Executable size"
	@echo
	@du -0 -k $* | cut -f1
	@echo
	@echo "#### Run"
	@echo
	@echo "\`\`\`"
	$(TIME) $*/$*
	@echo
