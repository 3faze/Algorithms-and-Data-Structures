#       2
#      / \
#     3   4
#    / \
#   5   6
#

class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


nodeA = Node(2)
nodeB = Node(3)
nodeC = Node(5)
nodeD = Node(6)
nodeE = Node(4)

nodeA.left = nodeB
nodeA.right = nodeE
nodeB.left = nodeC
nodeB.right = nodeD

#recursive approach

def find_sum(root):
    total = 0
    if root == None:
        return 0
    return root.data + find_sum(root.right) + find_sum(root.left)

print(find_sum(nodeA))
