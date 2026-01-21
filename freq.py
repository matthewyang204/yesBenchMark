import os
import subprocess
import sys
import time

from yaspin import yaspin
from yaspin.spinners import Spinners

from resources import *

def run_freq_bench(multicore=False, core=0):
    if platform.system() == "Darwin":
        print("This benchmark requires sudo privileges on macOS, please enter your password if prompted:")
        os.system("sudo -v")
    elif platform.system() == "Linux":
        pass
    else:
        raise PlatformNotSupportedError("Frequency benchmark is only supported on Linux and macOS.")
    spinner = yaspin(Spinners.line)
    print("Running frequency benchmark for 30 seconds...")
    result_30sec = []
    process = subprocess.Popen(['taskset', '-c', str(core), 'yes'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    end = time.time() + 30
    if not multicore:
        spinner.start()
    while time.time() < end:
        time.sleep(1)
        result_30sec.append(get_proc_mhz()[core])
    if not multicore:
        spinner.stop()
    process.terminate()
    print("Running frequency benchmark for 60 seconds...")
    result_60sec = []
    process = subprocess.Popen(['taskset', '-c', str(core), 'yes'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    end = time.time() + 60
    if not multicore:
        spinner.start()
    while time.time() < end:
        time.sleep(1)
        result_60sec.append(get_proc_mhz()[core])
    if not multicore:
        spinner.stop()
    process.terminate()
    return result_30sec, result_60sec