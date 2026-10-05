from multiprocessing import Process
import os

def calculate_sum(numbers):
    sum = 0
    for number in numbers:
        sum += number
    print(sum, os.getpid())

if __name__ == '__main__':
    arr1 = [1,2,3,4,5]
    arr2 = [2,3,4,5,6]

    num_arr = [arr1, arr2]

    processes = [Process(target = calculate_sum, args=(arr,)) for arr in num_arr]

    for process in processes:
        process.start()

    for process in processes:
        process.join() #wait for procees to complete



    # for i in range(len(arr1)):
    #     arr1[i] *= 2
    # print(arr1)

    # arr = [2*num for num in arr1]

