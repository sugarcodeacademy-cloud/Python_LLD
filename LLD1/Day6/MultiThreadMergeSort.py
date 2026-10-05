from threading import Thread
def merge_sort(arr):
    n = len(arr)
    if n <= 1: return arr

    mid = n//2
    left = []
    right = []
    #create threads
    t1 = Thread(target=lambda : left.extend(merge_sort(arr[:mid])), name="MergeThread - LEFT")
    t2 = Thread(target=lambda : right.extend(merge_sort(arr[mid:])), name="MergeThread - RIGHT")

    print(f"Created: {t1.name}")
    print(f"Created: {t2.name}")

    #start threads
    t1.start()
    t2.start()

    #wait for both threads to complete
    t1.join()
    t2.join()

    return merge(left, right)

def merge(left, right):
    result =[]
    i = j = 0
    while i< len(left) and j<len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result

numbers = [38,12, 27, 43, 9 , 31, 18]
print(merge_sort(numbers))