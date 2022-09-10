import code
import sys

def huffman_encoding(data):
    pass

def huffman_decoding(data,tree):
    pass


# helper functions
def frequency_counter(string):
    frequency_dict = {}
    if string is None:
        return "EMpty string"
    for char in string:
        if char not in frequency_dict:
            frequency_dict[char] = 1
        if char in frequency_dict:
            frequency_dict[char] += 1
    return list(sorted(frequency_dict.items(), key=lambda item: item[1], reverse=True))

class Node:
    def __init__(self, value, binarycode=0, char='*'):
        self.value = value
        self.char = char
        self.binarycode = binarycode
        self.leftChild = None
        self.rightChild = None
        
        
def build_huff(frequency_list):
    tree = []
    while len(frequency_list) > 1:
        new_node_value = frequency_list[-1][1] + frequency_list[-2][1]
        new_node = Node(new_node_value)
        new_node.leftChild = Node(frequency_list[-1][0], 0, frequency_list[-1][1])
        new_node.leftChild = Node(frequency_list[-2][0], 0, frequency_list[-2][1])
        frequency_list.pop()
        frequency_list.pop()
        frequency_list.insert(0, new_node_value)
    return frequency_list

print(build_huff(frequency_counter("THis is a trial")))

         
    
print(frequency_counter("chicken chips cheese cheetos"))
# if __name__ == "__main__":
#     codes = {}

#     a_great_sentence = "The bird is the word"

#     print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
#     print ("The content of the data is: {}\n".format(a_great_sentence))

#     encoded_data, tree = huffman_encoding(a_great_sentence)

#     print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
#     print ("The content of the encoded data is: {}\n".format(encoded_data))

#     decoded_data = huffman_decoding(encoded_data, tree)

#     print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
#     print ("The content of the encoded data is: {}\n".format(decoded_data))
