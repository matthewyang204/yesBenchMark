import subprocess
import time
import psutil

from yaspin import yaspin
from yaspin.spinners import Spinners

from .resources import *
from .freq import *
from .exceptions import *

def run_stress_bench():
    spinner = yaspin(Spinners.line)
    print("Running stress benchmark for 30 seconds...")
    result_30sec = []
    process = subprocess.Popen(['yes'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    end = time.time() + 30
    spinner.start()
    nothingInParticular = psutil.cpu_percent(interval=None) # initialize psutil
    while time.time() < end:
        result_30sec.append(psutil.cpu_percent(interval=1))
    spinner.stop()
    process.terminate()
    print("Running stress benchmark for 60 seconds...")
    result_60sec = []
    process = subprocess.Popen(['yes'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    end = time.time() + 60
    spinner.start()
    nothingInParticular = psutil.cpu_percent(interval=None) # initialize psutil again
    while time.time() < end:
        result_60sec.append(psutil.cpu_percent(interval=1))
    spinner.stop()
    process.terminate()
    return result_30sec, result_60sec