all: bench-go bench-pony bench-elixir bench-rust

bench-%:
	cd $*; $(MAKE)
