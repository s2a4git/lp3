import random
import time


# ------------------ Deterministic Quick Sort ------------------
def deterministic_quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[-1]  # fixed pivot → last element
    left = [x for x in arr[:-1] if x <= pivot]
    right = [x for x in arr[:-1] if x > pivot]
    return deterministic_quick_sort(left) + [pivot] + deterministic_quick_sort(right)


# ------------------ Randomized Quick Sort ------------------
def randomized_quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot_index = random.randint(0, len(arr) - 1)
    pivot = arr[pivot_index]  # random pivot
    rest = arr[:pivot_index] + arr[pivot_index + 1 :]
    left = [x for x in rest if x <= pivot]
    right = [x for x in rest if x > pivot]
    return randomized_quick_sort(left) + [pivot] + randomized_quick_sort(right)


# ------------------ Analysis / Execution ------------------
arr = [34, 12, 5, 66, 1, 90, 23, 7, 50]

start = time.time()
det_sorted = deterministic_quick_sort(arr)
det_time = time.time() - start

start = time.time()
rand_sorted = randomized_quick_sort(arr)
rand_time = time.time() - start

print("Original:", arr)
print("Deterministic Quick Sort:", det_sorted, "Time:", det_time)
print("Randomized Quick Sort:", rand_sorted, "Time:", rand_time)
