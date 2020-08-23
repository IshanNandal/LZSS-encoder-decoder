# Name: Ishan Nandal
# Student ID: 28278046
import heapq
from binary_tree import Node
from binary_tree import BinaryTree


# Takes in a min heap as a parameter, eg [(2, 'c'), (6, 'b'), (7, 'e'), (10, '_')]
def generate_binary_tree(priority_queue):
    intermediate_binary_trees = []

    while len(priority_queue) >= 2:

        smallest = heapq.heappop(priority_queue)
        second_smallest = heapq.heappop(priority_queue)
        root = Node(smallest[1] + second_smallest[1], smallest[0] + second_smallest[0])

        root.left = Node(smallest[1], smallest[0])
        root.right = Node(second_smallest[1], second_smallest[0])

        if len(root.left.string) > 1:
            for i in range(len(intermediate_binary_trees)):
                if intermediate_binary_trees[i].root.string == root.left.string:
                    root.left = intermediate_binary_trees[i].root

        if len(root.right.string) > 1:
            for i in range(len(intermediate_binary_trees)):
                if intermediate_binary_trees[i].root.string == root.right.string:
                    root.right = intermediate_binary_trees[i].root

        intermediate_binary_tree = BinaryTree(root)
        intermediate_binary_trees.append(intermediate_binary_tree)

        heapq.heappush(priority_queue, (root.value, root.string))

    return intermediate_binary_trees[-1]


path_dictionary = {}


# Returns a dictionary with characters as keys and their bit-path as values
def leaf_paths(root):
    if root:

        if root.left:
            root.left.path = root.path + "0"
        if root.right:
            root.right.path = root.path + "1"

        leaf_paths(root.left)
        leaf_paths(root.right)

        if root.right and len(root.right.string) == len(root.string) - 1:
            path_dictionary[root.left.string] = root.left.path
        if root.left and len(root.left.string) == len(root.string) - 1:
            path_dictionary[root.right.string] = root.right.path

    return path_dictionary


def huffman_encoder(text):
    # Dictionary of unique characters
    character_dictionary = {}

    for character in text:
        if character not in character_dictionary:
            character_dictionary[character] = 1
        else:
            character_dictionary[character] += 1

    # Priority queue
    priority_queue = []
    for character in character_dictionary:
        heapq.heappush(priority_queue, (character_dictionary[character], character))

    generated_tree = generate_binary_tree(priority_queue)
    bit_paths = leaf_paths(generated_tree.root)
    return bit_paths


if __name__ == "__main__":
    """
    min_heap1 = [(2, 'c'), (6, 'b'), (7, 'e'), (10, '_'), (10, 'd'), (11, 'a')]
    tree1 = generate_binary_tree(min_heap1)
    path_dictionary1 = leaf_paths(tree1.root)

    print(leaf_paths(tree1.root))
    # print(path_dictionary1['c'])
    """

    text1 = "aacaacabcaba"
    print(huffman_encoder(text1))
