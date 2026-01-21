import sys
import platform

from core import *
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
        run_bench("time")

if __name__ == "__main__":
    main()