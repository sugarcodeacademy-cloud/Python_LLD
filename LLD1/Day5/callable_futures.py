from concurrent.futures import ThreadPoolExecutor, as_completed

import time

def calculate_sum(data):
    return sum(data)

data_list=[[1,2,3,4,5],[40,50,30,10,22,34,55,66],[10,20,30,40,50], [40,50,30,10,22,34,55,66, 88, 99, 110],[30, 30, 40, 50, 70],[40,50,30,10,22,34,55,66]]
with ThreadPoolExecutor(max_workers=1) as executor:
        futures = []
        for data in data_list:
           futures.append(executor.submit(calculate_sum, data))


        for future in as_completed(futures):
            print(future.done())
            print(future.result())


