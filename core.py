import subprocess
import time

from yaspin import yaspin
from yaspin.spinners import Spinners

def run_bench(mode):
    global spinner

    if mode == "time":
        print("Running time benchmark for 30 seconds...")
        result_30sec = 0
        process = subprocess.Popen(['yes'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        end = time.time() + 30
        with yaspin(Spinners.line):
            while time.time() < end:
                line = process.stdout.readline()
                result_30sec += 1
        process.terminate()
        print("Running time benchmark for 60 seconds...")
        result_60sec = 0
        process = subprocess.Popen(['yes'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        end = time.time() + 60
        with yaspin(Spinners.line):
            while time.time() < end:
                line = process.stdout.readline()
                result_60sec += 1
        process.terminate()
        return result_30sec, result_60sec