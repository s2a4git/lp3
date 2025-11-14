import time


# ------------------ Naive String Matching ------------------
def naive_search(text, pattern):
    n, m = len(text), len(pattern)
    matches = []

    for i in range(n - m + 1):
        if text[i : i + m] == pattern:
            matches.append(i)
    return matches


# ------------------ Rabin-Karp String Matching ------------------
def rabin_karp(text, pattern, d=256, q=101):  # q = prime number
    n, m = len(text), len(pattern)
    p_hash = 0
    t_hash = 0
    h = 1
    matches = []

    # Pre-compute h = (d^(m-1)) % q
    for _ in range(m - 1):
        h = (h * d) % q

    # Initial hash of pattern and first window
    for i in range(m):
        p_hash = (d * p_hash + ord(pattern[i])) % q
        t_hash = (d * t_hash + ord(text[i])) % q

    # Slide over text
    for i in range(n - m + 1):
        if p_hash == t_hash:
            if text[i : i + m] == pattern:  # Double-check match
                matches.append(i)

        # Compute next window hash
        if i < n - m:
            t_hash = (d * (t_hash - ord(text[i]) * h) + ord(text[i + m])) % q
            if t_hash < 0:
                t_hash += q

    return matches


# ------------------ Comparison ------------------
text = "AABAACAADAABAABA"
pattern = "AABA"

start = time.time()
naive_res = naive_search(text, pattern)
naive_time = time.time() - start

start = time.time()
rk_res = rabin_karp(text, pattern)
rk_time = time.time() - start

print("Text:", text)
print("Pattern:", pattern)
print("\nNaive Matches at:", naive_res)
print("Rabin-Karp Matches at:", rk_res)

print("\nNaive Time:", naive_time)
print("Rabin-Karp Time:", rk_time)
