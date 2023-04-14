#linked list

#1-2-3-4-5

class Node:
	def __init__(self, data):
		self.data = data
		self.next = Node
		
class linkedList:
	def __init__(self, nodeA, nodeB, nodeC):
		self.nodeA = Node(nodeA)
		self.nodeB = Node(nodeB)
		self.nodeC = Node(nodeC)
		
		self.nodeA.next = self.nodeB
		self.nodeB.next = self.nodeC	
		
list1 = linkedList(1, 2, 3)

print(list1.nodeB.next.data)
