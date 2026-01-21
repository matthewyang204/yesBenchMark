import subprocess
import time

from yaspin import yaspin
from yaspin.spinners import Spinners

def run_timed_bench():
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

def multicore():
    pass

def run_bench(mode):
    global spinner

    if mode == "time":
        results = run_timed_bench()
        avg_30sec = results[0] / 30
        avg_60sec = results[1] / 60
        print("Results for time-based benchmark:")
        print(f"Lines in 30 seconds: {results[0]}")
        print(f"Lines in 60 seconds: {results[1]}")
        print("Averages:")
        print(f"Average lines per second (30 sec): {avg_30sec}")
        print(f"Average lines per second (60 sec): {avg_60sec}")