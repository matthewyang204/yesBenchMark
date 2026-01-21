import os
import sys
import platform
import subprocess
import time

from exceptions import *

args = sys.argv

if platform.system() == "Windows" and '--allow-windows' not in args:
    raise PlatformNotSupportedError("Windows cannot possibly have coreutils installed and is not a supported configuration. Even if it does, it is under Cygwin and has way too much overhead to be accurate. Please install Linux or another UNIX-like system on your computer to continue.")
    
def main():
    if '--help' in args or '-h' in args:
        print("Usage: python main.py [options]")
        print("Options:")
        print("  --help, -h          Show this help message")
        print("  --mode=MODE         Run specific mode of benchmark")
        sys.exit(0)
    
    if '--mode=time' in args:
        mode = "time"
    else:
        mode = "all"

    if mode == "all":
        results = run_bench("time")
        avg_30sec = results[0] / 30
        avg_60sec = results[1] / 60
        print("Results for time-based benchmark:")
        print(f"Lines in 30 seconds: {results[0]}")
        print(f"Lines in 60 seconds: {results[1]}")
        print("Averages:")
        print(f"Average lines per second (30 sec): {avg_30sec}")
        print(f"Average lines per second (60 sec): {avg_60sec}")

if __name__ == "__main__":
    main()