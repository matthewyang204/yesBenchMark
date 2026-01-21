import sys
import platform

from core import *
from exceptions import *
from resources import *

args = sys.argv

if platform.system() == "Windows" and '--allow-windows' not in args:
    raise PlatformNotSupportedError("Windows cannot possibly have coreutils installed and is not a supported configuration. Even if it does, it is under Cygwin and has way too much overhead to be accurate. Please install Linux or another UNIX-like system on your computer to continue.")

def print_version():
    print("yesbenchmark, version 1.0.0")
    print("(C) 2026 Matthew Yang (杨佳明)")

def print_usage():
    print("Usage: python main.py [options]")
    print("Options:")
    print("  --help, -h          Show this help message")
    print("  --mode=MODE         Run specific mode of benchmark")
    print("")
    print("Modes:")
    print("all                   Run all modes of benchmarks")
    print("time                  Run time-bound benchmark")
    print("multicore             Run time-bound benchmark for all cores")
    print("freq                  Run frequency-bound benchmark")
    print("multi-freq            Run multi-core version of frequency-bound benchmark")
    print("")
    print("This benchmarking program does not have Super DNA Powers.")

def main():
    if '--help' in args or '-h' in args:
        print_usage()
        sys.exit(0)
    elif '--version' in args or '-v' in args:
        print_version()
        sys.exit(0)
    
    if len(args) > 1:
        if args[1] == "dna":
            if len(args) <= 2:
                dna()
            else:
                dna(args[2])
            sys.exit(0)
    
    if '--mode=time' in args:
        mode = "time"
    elif '--mode=multicore' in args:
        mode = "multicore"
    elif '--mode=freq' in args:
        mode = "freq"
    elif '--mode=multi-freq' in args:
        mode = "multi-freq"
    else:
        mode = "all"

    if mode == "all":
        print(f"Running time benchmark:")
        run_bench("time")
        print(f"Running multicore benchmark:")
        run_bench("multicore")
        print(f"Running freq benchmark:")
        run_bench("freq")
        print(f"Running multi-freq benchmark:")
        run_bench("multi-freq")
    else:
        run_bench(mode)

if __name__ == "__main__":
    main()