import heapq


# Node class for tree
class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq  # needed for heap


# Build Huffman Tree (Greedy)
def build_tree(freq):
    heap = [Node(ch, f) for ch, f in freq.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        a = heapq.heappop(heap)  # smallest
        b = heapq.heappop(heap)  # second smallest
        merged = Node(None, a.freq + b.freq)
        merged.left, merged.right = a, b
        heapq.heappush(heap, merged)

    return heap[0]  # root


# Generate codes by DFS
def get_codes(root, code="", codes=None):
    if codes is None:
        codes = {}
    if root.char is not None:  # leaf node
        codes[root.char] = code
        return codes
    get_codes(root.left, code + "0", codes)
    get_codes(root.right, code + "1", codes)
    return codes


# Driver
text = "huffmanencodingexample"

# Step 1: frequency count
freq = {}
for ch in text:
    freq[ch] = freq.get(ch, 0) + 1

# Step 2: build Huffman tree
root = build_tree(freq)

# Step 3: generate codes
codes = get_codes(root)

# Step 4: encode
encoded = "".join(codes[ch] for ch in text)

print("Frequencies:", freq)
print("Codes:", codes)
print("Encoded:", encoded)
