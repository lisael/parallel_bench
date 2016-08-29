include ../Makefile.in

all: title bench-montecarlo

title:
	@echo "## Rust"
	@echo

bench-%: $*
	-@rm -rf $*/target
	@echo "### $*"
	@echo
	@echo "#### Version"
	@echo
	rustc --version
	@echo
	@echo "#### Build"
	@echo
	-@cd $*; cargo update
	@echo "\`\`\`"
	cd $*; $(TIME) cargo build --release
	@echo
	@echo "#### Executable size"
	@echo
	@du -0 -k $*/target/release/$* | cut -f1
	@echo
	@echo "#### Run"
	@echo
	@echo "\`\`\`"
	$(TIME) $*/target/release/$*
	@echo
