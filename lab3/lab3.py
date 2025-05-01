import heapq
from collections import Counter

class Node:
    def __init__(self, char=None, freq=0):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    # For priority queue comparison
    def __lt__(self, other):
        return self.freq < other.freq

def build_frequency_table(text):
    return Counter(text)

def build_huffman_tree(freq_table):
    heap = [Node(char, freq) for char, freq in freq_table.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        node1 = heapq.heappop(heap)
        node2 = heapq.heappop(heap)
        merged = Node(freq=node1.freq + node2.freq)
        merged.left = node1
        merged.right = node2
        heapq.heappush(heap, merged)

    return heap[0]

def build_codes(node, prefix="", code_map=None):
    if code_map is None:
        code_map = {}
    if node:
        if node.char is not None:
            code_map[node.char] = prefix
        build_codes(node.left, prefix + "0", code_map)
        build_codes(node.right, prefix + "1", code_map)
    return code_map

def huffman_encode(text, code_map):
    return ''.join(code_map[char] for char in text)

def huffman_decode(encoded_text, root):
    decoded = []
    node = root
    for bit in encoded_text:
        node = node.left if bit == '0' else node.right
        if node.char:
            decoded.append(node.char)
            node = root
    return ''.join(decoded)

def compression_ratio(original_text, encoded_text):
    original_bits = len(original_text) * 8
    encoded_bits = len(encoded_text)
    return round(original_bits / encoded_bits, 2)

if __name__ == "__main__":
    input_text = "Theory of information and coding"

    # Frequency table
    freq_table = build_frequency_table(input_text)

    # Huffman tree and code map
    root = build_huffman_tree(freq_table)
    code_map = build_codes(root)

    print("Huffman Code Table:")
    for char, code in code_map.items():
        print(f"{char}: {code}")

    # Encoding
    encoded = huffman_encode(input_text, code_map)
    print(f"\nEncoded Text: {encoded}")

    # Decoding
    decoded = huffman_decode(encoded, root)
    print(f"\nDecoded Text: {decoded}")

    # Compression efficiency
    ratio = compression_ratio(input_text, encoded)
    print(f"\nCompression Ratio: {ratio}")
