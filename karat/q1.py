"""
Suppose we have a list of parent-child pairs that represent a family tree:

    1   2    4
     \ /   / | \
      3   5  8  9
       \ / \     \
        6   7    11

parent_child_pairs = [
    (1, 3), (2, 3), (3, 6), (5, 6),
    (5, 7), (4, 5), (4, 8), (4, 9), (9, 11)
]

For example, 1 is a parent of 3, and 4 is a parent of 5, 8 and 9.

Write a function that takes parent_child_pairs as input, as well as two people, A and B, and returns True if A is a parent of B. Otherwise the function returns False

Sample input and output:

is_parent_of(parent_child_pairs, 1, 3) --> True
is_parent_of(parent_child_pairs, 3, 1) --> False # parent is always first in pair
is_parent_of(parent_child_pairs, 1, 9) --> False
is_parent_of(parent_child_pairs, 1, 6) --> False # not transitive, not grandparents

Complexity Analysis variables:

n: the number of pairs in the input
"""

parent_child_pairs = [
    (1, 3),
    (2, 3),
    (3, 6),
    (5, 6),
    (5, 7),
    (4, 5),
    (4, 8),
    (4, 9),
    (9, 11),
]


def is_parent_of(parent_child_pairs, A, B):
    # Construct an adjacency list to represent the parent-child relationships
    adjacency_list = {}
    for parent, child in parent_child_pairs:
        if parent not in adjacency_list:
            adjacency_list[parent] = []
        adjacency_list[parent].append(child)

    # Check if there exists a path from A to B using a visited set to avoid cycles
    visited = set()

    def dfs(node):
        if node == B:
            return True

        visited.add(node)

        for neighbor in adjacency_list.get(node, []):
            if neighbor not in visited and dfs(neighbor):
                return True

        return False

    return dfs(A)


print(is_parent_of(parent_child_pairs, 1, 3))
