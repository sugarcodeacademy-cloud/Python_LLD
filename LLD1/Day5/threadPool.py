from concurrent.futures import ThreadPoolExecutor

import time

def task(n):
    time.sleep(3)
    print(f"Processing {n}")


with ThreadPoolExecutor(max_workers=10) as executor:
    for i in range(1, 100):
        executor.submit(task, i)
