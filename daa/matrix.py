import threading
import time


# ------------------ Normal Matrix Multiplication ------------------
def matmul(A, B):
    n = len(A)
    m = len(B[0])
    p = len(B)
    C = [[0] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            for k in range(p):
                C[i][j] += A[i][k] * B[k][j]
    return C


# ------------------ Multithreaded (one thread per row) ------------------
def compute_row(A, B, C, row):
    m = len(B[0])
    p = len(B)
    for j in range(m):
        for k in range(p):
            C[row][j] += A[row][k] * B[k][j]


def matmul_threaded(A, B):
    n = len(A)
    C = [[0] * len(B[0]) for _ in range(n)]
    threads = []

    for i in range(n):
        t = threading.Thread(target=compute_row, args=(A, B, C, i))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()
    return C


# ------------------ Time Utility ------------------
def time_taken(func, A, B):
    start = time.time()
    func(A, B)
    return time.time() - start


# ------------------ Main ------------------
A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

B = [[1, 0, 1], [0, 1, 0], [1, 0, 1]]

print("Normal:", matmul(A, B))
print("Threaded:", matmul_threaded(A, B))

# Measure performance
t1 = time_taken(matmul, A, B)
t2 = time_taken(matmul_threaded, A, B)

print("\nTime Normal       :", t1)
print("Time Multithreaded:", t2)
