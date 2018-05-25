import random
import time


def findsmallest(arr):
    smallest = arr[0]
    smalles_index = 0

    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smalles_index = i
            smallest = arr[i]

    return smalles_index


def findlargest(arr):
    largest = arr[0]
    largest_index = 0

    for i in range(1, len(arr)):
        if arr[i] > largest:
            largest_index = i
            largest = arr[i]

    return largest_index

def selectionsort(arr):
    newArr = []

    for i in range(len(arr)):
        smallest = findlargest(arr)
        newArr.append(arr.pop(smallest))

    return newArr


def selectionsort2(arr):
    for i in range(0, len(arr)):
        for j in range(i+1, len(arr)):
            if arr[j] > arr[i]:
                arr[i], arr[j] = arr[j], arr[i]

    return arr

def selectionsort3(arr):
    n = len(arr)

    for i in range(0, n//2):
        largest = arr[i]
        largest_index = i
        smallest = arr[n-i-1]
        smallest_index = n-i-1
        for j in range(i+1, n-i):
            if arr[j] > largest:
                largest = arr[j]
                largest_index = j
            if arr[j] < smallest:
                smallest = arr[j]
                smallest_index = j
        arr[i], arr[largest_index] = arr[largest_index], arr[i]
        arr[n-i-1], arr[smallest_index] = arr[smallest_index], arr[n-i-1]

    return arr


nums1 = []
nums2 = []
for i in range(10000):
  num = random.randint(1, 100000)
  nums1.append(num)
  nums2.append(num)

print(selectionsort([5, 3, 6, 2, 2, 10]))

print("selection sort 2", time.time())
selectionsort2(nums1)
print('selection sort 3', time.time())
selectionsort3(nums2)
print('end', time.time())
