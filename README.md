# Parallel Benchmarks

A set of benchmarks for parallel programming languages

TL;DR: [raw results](https://github.com/lisael/parallel_bench/blob/master/summary.md)

## Languages

### Go

I used to love it. It's asynchronous model with coroutines and channels is still very pleasant. Its strange inheritance model encouraging copy-and-paste and code generator coding style is annoying.

### Elixir

The new kid. I played a little with it.

### Pony

The next big thing, I hope.

### Rust


## Algorithms

The algorithms are chosen because they benefit from parallel execution. They may not be fully optimised, but we try to port the same algorithm in all languages. The most difficult part is porting to functional languages (e.g recursion + accumulator rather than list traversal). In all case we try to use the most idiomatic form of each language, without micro-optimisations.

## Disclaimer

I wrote those to test [Ponyc](https://github.com/ponylang/ponyc) performances.
