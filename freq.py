import os
import subprocess
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
    if platform.system() == "Linux":
        process = subprocess.Popen(['taskset', '-c', str(core), 'yes'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    elif platform.system() == "Darwin":
        process = subprocess.Popen(['yes'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    end = time.time() + 30
    if not multicore:
        spinner.start()
    if platform.system() == "Linux":
        while time.time() < end:
            time.sleep(1)
            result_30sec.append(get_proc_mhz()[core])
    elif platform.system() == "Darwin":
        while time.time() < end:
            time.sleep(1)
            freqs = get_darwin_mhz()
            if not multicore:
                if freqs:
                    max_freq = max(freqs)
                    result_30sec.append(max_freq)
            else:
                coreFreq = freqs[core]
                result_30sec.append(coreFreq)
    if not multicore:
        spinner.stop()
    process.terminate()
    print("Running frequency benchmark for 60 seconds...")
    result_60sec = []
    if platform.system() == "Linux":  
        process = subprocess.Popen(['taskset', '-c', str(core), 'yes'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    elif platform.system() == "Darwin":
        process = subprocess.Popen(['yes'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    end = time.time() + 60
    if not multicore:
        spinner.start()
    if platform.system() == "Linux":
        while time.time() < end:
            time.sleep(1)
            result_60sec.append(get_proc_mhz()[core])
    elif platform.system() == "Darwin":
        while time.time() < end:
            time.sleep(1)
            freqs = get_darwin_mhz()
            if multicore:
                if freqs:
                    max_freq = max(freqs)
                    result_60sec.append(max_freq)
            else:
                coreFreq = freqs[core]
                result_60sec.append(coreFreq)
    if not multicore:
        spinner.stop()
    process.terminate()
    return result_30sec, result_60sec

def run_freq_bench_multicore(n):
    def run_freq_bench_multicore(core=0):
        return run_freq_bench(multicore=True, core=core)
    
    if platform.system() == "Darwin":
        print("This benchmark requires sudo privileges on macOS, please enter your password if prompted:")
        os.system("sudo -v")
    results_30sec = ()
    results_60sec = ()
    coreCount = os.cpu_count()
    spinner = yaspin(Spinners.line)
    spinner.start()
    results_30sec, results_60sec = multirun_coreArg(run_freq_bench_multicore, coreCount)
    spinner.stop()
    return results_30sec, results_60sec