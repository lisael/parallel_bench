## Go

### montecarlo

#### Version

go1.6.3 linux/amd64

#### Build

```

```

| Command | Wall Clock (s) | Max Mem (Kb) |
|:---|---:|---:|
| go build montecarlo | 0.54 | 42780 |

#### Executable size

2284

#### Run

```
3.14187056

```

| Command | Wall Clock (s) | Max Mem (Kb) |
|:---|---:|---:|
| ./montecarlo | 1.48 | 2068 |

## Pony

### montecarlo

#### Version

0.3.0-5-gb2cdd03 [release]

#### Build

```
Building builtin -> /usr/local/lib/pony/0.3.0-5-gb2cdd03/packages/builtin
Building montecarlo -> /home/bdupuis/projects/perso/parallel_bench/pony/montecarlo
Building time -> /usr/local/lib/pony/0.3.0-5-gb2cdd03/packages/time
Building ponytest -> /usr/local/lib/pony/0.3.0-5-gb2cdd03/packages/ponytest
Building collections -> /usr/local/lib/pony/0.3.0-5-gb2cdd03/packages/collections
Building random -> /usr/local/lib/pony/0.3.0-5-gb2cdd03/packages/random
Generating
 Reachability
 Selector painting
 Data prototypes
 Data types
 Function prototypes
 Functions
 Descriptors
Optimising
Writing build/montecarlo.o
Linking build/montecarlo

```

| Command | Wall Clock (s) | Max Mem (Kb) |
|:---|---:|---:|
| ponyc -o build montecarlo | 1.70 | 228992 |

#### Executable size

140

#### Run

```
3.14164

```

| Command | Wall Clock (s) | Max Mem (Kb) |
|:---|---:|---:|
| build/montecarlo | 0.60 | 2560 |

## Elixir

### montecarlo

#### Version

Erlang/OTP 18 [erts-7.3.1.1] [source] [64-bit] [smp:4:4] [async-threads:10] [kernel-poll:false] - Elixir 1.2.0

#### Build

```
lib/montecarlo.ex:2: warning: variable args is unused
lib/montecarlo.ex:25: warning: erlang:now/0: Deprecated BIF. See the "Time and Time Correction in Erlang" chapter of the ERTS User's Guide for more information.
Compiled lib/montecarlo.ex
Generated montecarlo app
Consolidated List.Chars
Consolidated String.Chars
Consolidated Collectable
Consolidated Enumerable
Consolidated IEx.Info
Consolidated Inspect
Generated escript montecarlo with MIX_ENV=prod

```

| Command | Wall Clock (s) | Max Mem (Kb) |
|:---|---:|---:|
| mix escript.build | 1.00 | 64988 |

#### Executable size

20

#### Run

```
3.14163308

```

| Command | Wall Clock (s) | Max Mem (Kb) |
|:---|---:|---:|
| montecarlo/montecarlo | 25.82 | 25520 |

## Rust

### montecarlo

#### Version

rustc 1.11.0 (9b21dcd6a 2016-08-15)

#### Build

    Updating registry `https://github.com/rust-lang/crates.io-index`
```
   Compiling libc v0.2.15
   Compiling rand v0.3.14
   Compiling montecarlo v0.1.0 (file:///home/bdupuis/projects/perso/parallel_bench/rust/montecarlo)

```

| Command | Wall Clock (s) | Max Mem (Kb) |
|:---|---:|---:|
| cargo build --release | 6.47 | 143624 |

#### Executable size

756

#### Run

```
3.14155344

```

| Command | Wall Clock (s) | Max Mem (Kb) |
|:---|---:|---:|
| montecarlo/target/release/montecarlo | 0.34 | 2712 |

