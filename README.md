# yesBenchMark
yesBenchMark is a crazy tool for benchmarking the CPU in UNIX & UNIX-like systems. It abuses the `yes` command to load the CPU and measures CPU utilization, speed, and compute.

<img src="https://raw.githubusercontent.com/matthewyang204/yesBenchMark/master/assets/yesbenchmark-demo.gif" width="547" alt="yesBenchMark demo (animated)">

# Features
- Extremely tiny & light
- Can run on extremely old hardware (OS X 10.4 Tiger is oldest it can run on of all the stuff out there, with a modest G3)
- Can do a ton of different modes, varying in load from light to extremely punishing to see how far you can push your CPU:
    - `time` - See how much the CPU can output in 30 & 60 seconds respectively in a single thread (`yes`)
    - `multicore` - Multi-core version of the `time` benchmark
    - `freq` - Bench how fast your CPU core can turbo
    - `multi-freq` - Multi-core version of `freq` benchmark
    - `stress` - See how little of the total CPU a single thread can use, also includes a stability measurement
    - `compute` - Check how long it takes the CPU to compute 27,000,000,000 hunks of data (each hunk is a single `y\n`)
    - `compute-xt` - `compute` benchmark but with 10x the hunks
- Written in Python & extremely portable, so runs almost anywhere
- Probably one of the most practical benchmarks out there - measures CPU load, CPU frequency, and other things encouuntered in day-to-day workloads; none of the shenanigans that most tools use to grade your CPU's performance

# Usage
```
Usage: yesbenchmark [options]
Options:
  --help, -h          Show this help message
  --mode=MODE         Run specific mode of benchmark

Modes:
all                   Run all modes of benchmarks
time                  Run time-bound benchmark
multicore             Run time-bound benchmark for all cores
freq                  Run frequency-bound benchmark
multi-freq            Run multi-core version of frequency-bound benchmark
stress                Run stress/utilization benchmark
compute               Run compute benchmark (time taken depends on CPU speed)
compute-xt            Run a more extreme version of compute benchmark
```