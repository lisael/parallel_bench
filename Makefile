all: bench-go bench-pony bench-elixir

bench-%:
	cd $*; $(MAKE)
