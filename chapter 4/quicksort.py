import random
import time

def quick_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i < pivot]
        greater = [i for i in arr[1:] if i >= pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)


def quick_sort2(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        i = 0
        j = len(arr) - 1
        while i < j:
            while i < j and arr[j] >= pivot:
                j -= 1

            if i < j:
                arr[i] = arr[j]
                i += 1

            while i < j and arr[i] < pivot:
                i += 1

            if i < j:
                arr[j] = arr[i]
                j -= 1

        arr[i] = pivot
        return quick_sort2(arr[:i]) + [pivot] + quick_sort2(arr[i+1:])


def quick_sort3(arr, l, r):
    if l >= r:
        return []

    pivot = arr[l]
    i = l
    j = r
    while i < j:
        while i < j and arr[j] >= pivot:
            j -= 1

        if i < j:
            arr[i] = arr[j]
            i += 1

        while i < j and arr[i] < pivot:
            i += 1

        if i < j:
            arr[j] = arr[i]
            j -= 1

    arr[i] = pivot
    return quick_sort3(arr, l, i) + [pivot] + quick_sort3(arr, i+1, r)

nums1 = []
nums2 = []
nums3 = []
arrlen = 10000000
for i in range(arrlen):
  num = random.randint(1, arrlen*10)
  nums1.append(num)
  nums2.append(num)
  nums3.append(num)

print(time.time())
quick_sort3(nums3, 0, arrlen-1)
print(time.time())
quick_sort2(nums2)
print(time.time())
quick_sort(nums1)
print(time.time())
