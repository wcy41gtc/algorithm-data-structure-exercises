import heapq
from collections import defaultdict

class HuffmanNode():
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(data):
    if not data:
        return None

    frequency = defaultdict(int)
    for char in data:
        frequency[char] += 1

    heap = [HuffmanNode(char, freq) for char, freq in frequency.items()]
    heapq.heapify(heap)

    if len(heap) == 1:
        # Special case: if there's only one unique character, create a dummy node
        only_node = heapq.heappop(heap)
        dummy_node = HuffmanNode(None, 0)
        merged = HuffmanNode(None, only_node.freq)
        merged.left = dummy_node
        merged.right = only_node
        heapq.heappush(heap, merged)

    while len(heap) > 1:
        node1 = heapq.heappop(heap)
        node2 = heapq.heappop(heap)
        merged = HuffmanNode(None, node1.freq + node2.freq)
        merged.left = node1
        merged.right = node2
        heapq.heappush(heap, merged)
    return heap[0]

def build_huffman_codes(tree, prefix="", codebook=None):

    if tree is None:
        return {}
    
    if codebook is None:
        codebook = {}

    if tree.char is not None:
        codebook[tree.char] = prefix or "0"  # Ensure at least "0" is assigned if prefix is empty
    else:
        if tree.left:
            build_huffman_codes(tree.left, prefix + "0", codebook)
        if tree.right:
            build_huffman_codes(tree.right, prefix + "1", codebook)


    return codebook

def huffman_encoding(data):
    if not isinstance(data, str):
        raise ValueError("Input must be a string")
    if not data:
        return "", None
    tree = build_huffman_tree(data)
    codebook = build_huffman_codes(tree)
    encoded_data = ''.join(codebook[char] for char in data)
    return encoded_data, tree

def huffman_decoding(data, tree):
    if tree is None:
        return ""
    elif not isinstance(tree, HuffmanNode):
        raise ValueError("Tree must be a Huffman tree")
    # Check if data contains only '0' and '1'
    if not all(bit in '01' for bit in data):
        raise ValueError("Data must contain only '0' and '1'")
    # Check if tree is a Huffman tree

    decoded_data = []
    current_node = tree

    for bit in data:
        if bit == '0':
            current_node = current_node.left
        else:
            current_node = current_node.right

        if current_node.char is not None:
            decoded_data.append(current_node.char)
            current_node = tree

    return ''.join(decoded_data)

def test_huffman_coding():
    # Test Case 1: Regular Input
    data1 = "The bird is the word"
    encoded_data1, tree1 = huffman_encoding(data1)
    decoded_data1 = huffman_decoding(encoded_data1, tree1)
    assert decoded_data1 == data1, "Test Case 1 Failed"
    print("Test Case 1 Passed")

    # Test Case 2: Empty Input (Edge Case)
    data2 = ""
    encoded_data2, tree2 = huffman_encoding(data2)
    decoded_data2 = huffman_decoding(encoded_data2, tree2)
    assert encoded_data2 == "", "Test Case 2 Failed"
    assert decoded_data2 == "", "Test Case 2 Failed"
    print("Test Case 2 Passed")

    # Test Case 3: Very Large Input (Edge Case)
    data3 = "b" * 1000000
    encoded_data3, tree3 = huffman_encoding(data3)
    decoded_data3 = huffman_decoding(encoded_data3, tree3)
    assert decoded_data3 == data3, "Test Case 3 Failed"
    print("Test Case 3 Passed")

    # Test Case 4: Invalid Input
    try:
        huffman_encoding(123)
    except ValueError:
        print("Test Case 4 Passed")
    else:
        print("Test Case 4 Failed")
    
    # Test Case 5: Empty Input
    data5 = ""
    encoded_data5, tree5 = huffman_encoding(data5)
    decoded_data5 = huffman_decoding(encoded_data5, tree5)
    assert decoded_data5 == data5, "Test Case 5 Failed"
    print("Test Case 5 Passed")
    
    # Test Case 6: Invalid Decoding Data
    try:
        huffman_decoding("012101", None)
    except ValueError:
        print("Test Case 6 Passed")
    else:
        print("Test Case 6 Failed")

    # Test Case 7: Invalid Decoding Tree
    try:
        huffman_decoding("010101", 123)
    except ValueError:
        print("Test Case 7 Passed")
    else:
        print("Test Case 7 Failed")

if __name__ == "__main__":
    test_huffman_coding()