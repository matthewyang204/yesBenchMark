from concurrent.futures import ProcessPoolExecutor

def multirun(func, n):
    x = []
    y = []

    with ProcessPoolExecutor() as ex:
        futures = [ex.submit(func, i) for i in range(n)]
        for f in futures:
            a, b = f.result()
            x.append(a)
            y.append(b)

    return x, y
