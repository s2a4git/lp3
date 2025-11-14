import time
import threading


# ------------------ Normal Merge Sort ------------------
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


# ------------------ Multithreaded Merge Sort ------------------
def threaded_merge_sort(arr):

    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    # Threads for each half
    t1 = threading.Thread(target=lambda l: l.append(merge_sort(left)), args=([],))
    t2 = threading.Thread(target=lambda r: r.append(merge_sort(right)), args=([],))

    t1.start()
    t2.start()
    t1.join()
    t2.join()

    # After threads complete
    sorted_left = merge_sort(left)
    sorted_right = merge_sort(right)
    return merge(sorted_left, sorted_right)


# ------------------ Time Analysis Function ------------------
def measure_time(func, arr):
    start = time.time()
    func(arr.copy())
    return time.time() - start


# ------------------ Main ------------------
# Best Case: Already sorted
best_case = [i for i in range(10000)]

# Worst Case: Reverse sorted
worst_case = best_case[::-1]

# Compare times
print("\n--- BEST CASE ---")
print("Normal Merge Sort:", measure_time(merge_sort, best_case))
print("Threaded Merge Sort:", measure_time(threaded_merge_sort, best_case))

print("\n--- WORST CASE ---")
print("Normal Merge Sort:", measure_time(merge_sort, worst_case))
print("Threaded Merge Sort:", measure_time(threaded_merge_sort, worst_case))
