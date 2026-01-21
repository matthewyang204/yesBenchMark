from concurrent.futures import ProcessPoolExecutor

def multirun(func, n):
    x = []
    y = []

    with ProcessPoolExecutor() as ex:
        futures = [ex.submit(func) for i in range(n)]
        for f in futures:
            a, b = f.result()
            x.append(a)
            y.append(b)

    return x, y

def get_proc_mhz():
    freqs = []
    with open("/proc/cpuinfo") as f:
        for line in f:
            if "cpu MHz" in line:
                freqs.append(float(line.split(":")[1].strip()))
    return freqs
