import os
import subprocess
import time

from yaspin import yaspin
from yaspin.spinners import Spinners

from resources import *
from freq import *

def run_timed_bench(multicore=False):
    spinner = yaspin(Spinners.line)
    print("Running time benchmark for 30 seconds...")
    result_30sec = 0
    process = subprocess.Popen(['yes'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    end = time.time() + 30
    if not multicore:
        spinner.start()
    while time.time() < end:
        chunk = process.stdout.read(65536)
        if not chunk:
            break
        result_30sec += chunk.count(b'\n')
    if not multicore:
        spinner.stop()
    process.terminate()
    print("Running time benchmark for 60 seconds...")
    result_60sec = 0
    process = subprocess.Popen(['yes'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    end = time.time() + 60
    if not multicore:
        spinner.start()
    while time.time() < end:
        chunk = process.stdout.read(65536)
        if not chunk:
            break
        result_60sec += chunk.count(b'\n')
    if not multicore:
        spinner.stop()
    process.terminate()
    return result_30sec, result_60sec

def multicore():
    cpucount = os.cpu_count()
    spinner = yaspin(Spinners.line)
    spinner.start()
    results_30sec, results_60sec = multirun(run_timed_bench_multicore, cpucount)
    spinner.stop()
    total_30sec = sum(results_30sec)
    total_60sec = sum(results_60sec)
    return results_30sec, results_60sec, total_30sec, total_60sec

def run_timed_bench_multicore():
    return run_timed_bench(multicore=True)

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
    
    elif mode == "multicore":
        results_30sec, results_60sec, total_30sec, total_60sec = multicore()
        for i in range(os.cpu_count()):
            print(f"Core #{i+1}:")
            print(f"  Lines in 30 seconds: {results_30sec[i]}")
            print(f"  Lines in 60 seconds: {results_60sec[i]}")
            avg_30sec = results_30sec[i] / 30
            avg_60sec = results_60sec[i] / 60
            print("  Averages:")
            print(f"    Average lines per second (30 sec): {avg_30sec}")
            print(f"    Average lines per second (60 sec): {avg_60sec}")
        print("All cores:")
        print(f"Total lines in 30 seconds: {total_30sec}")
        print(f"Total lines in 60 seconds: {total_60sec}")
        print("Averages:")
        avg_percore_30sec = total_30sec / os.cpu_count()
        avg_percore_60sec = total_60sec / os.cpu_count()
        print(f"Average lines per core (30 sec): {avg_percore_30sec}")
        print(f"Average lines per core (60 sec): {avg_percore_60sec}")
        avg_percore_30sec = avg_percore_30sec / 30
        avg_percore_60sec = avg_percore_60sec / 60
        print(f"Average lines per second per core (30 sec): {avg_percore_30sec}")
        print(f"Average lines per second per core (60 sec): {avg_percore_60sec}")
    
    elif mode == "freq":
        results_30sec, results_60sec = run_freq_bench()
        avg_30sec = sum(results_30sec) / len(results_30sec)
        avg_60sec = sum(results_60sec) / len(results_60sec)
        max_30sec = max(results_30sec)
        max_60sec = max(results_60sec)
        min_30sec = min(results_30sec)
        min_60sec = min(results_60sec)
        print("Results for frequency-based benchmark:")
        print(f"Frequencies in 30 seconds: {results_30sec}")
        print(f"Frequencies in 60 seconds: {results_60sec}")
        print("Averages:")
        print(f"Average frequency (30 sec): {avg_30sec} MHz")
        print(f"Average frequency (60 sec): {avg_60sec} MHz")
        print("Your cores reached the following maximum and minimum frequencies:")
        print(f"Maximum frequency (30 sec): {max_30sec} MHz")
        print(f"Maximum frequency (60 sec): {max_60sec} MHz")
        print(f"Minimum frequency (30 sec): {min_30sec} MHz")
        print(f"Minimum frequency (60 sec): {min_60sec} MHz")