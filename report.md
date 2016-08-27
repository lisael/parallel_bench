## Go

### montecarlo

#### Version

go1.6.3 linux/amd64

#### Build

```

```

| Command | Wall Clock (s) | Max Mem (Kb) |
|:---|---:|---:|
| go build montecarlo | 0.34 | 42196 |

#### Executable size

2284

#### Run

```
3.1416513999999998

```

| Command | Wall Clock (s) | Max Mem (Kb) |
|:---|---:|---:|
| ./montecarlo | 1.44 | 2076 |

## Pony

### montecarlo

#### Version

0.2.1-1068-g4ec8b31 [debug]

#### Build

```
Building builtin -> /usr/local/lib/pony/0.2.1-1068-g4ec8b31/packages/builtin
Building montecarlo -> /home/bdupuis/projects/perso/parallel_bench/pony/montecarlo
Building time -> /usr/local/lib/pony/0.2.1-1068-g4ec8b31/packages/time
Building ponytest -> /usr/local/lib/pony/0.2.1-1068-g4ec8b31/packages/ponytest
Building collections -> /usr/local/lib/pony/0.2.1-1068-g4ec8b31/packages/collections
Building random -> /usr/local/lib/pony/0.2.1-1068-g4ec8b31/packages/random
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
| ponyc -o build montecarlo | 2.82 | 228260 |

#### Executable size

296

#### Run

```
3.14166

```

| Command | Wall Clock (s) | Max Mem (Kb) |
|:---|---:|---:|
| build/montecarlo | 0.67 | 2588 |

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
| mix escript.build | 0.90 | 63004 |

#### Executable size

20

#### Run

```
3.14149904

```

| Command | Wall Clock (s) | Max Mem (Kb) |
|:---|---:|---:|
| montecarlo/montecarlo | 26.14 | 25444 |

