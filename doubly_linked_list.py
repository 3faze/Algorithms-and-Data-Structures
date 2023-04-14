#doubly linked list

#1-2-3-4-5

class Node:
	def __init__(self, data):
		self.data = data
		self.next = Node
		self.prev = Node
		
class linkedList:
	def __init__(self, nodeA, nodeB, nodeC):
		self.nodeA = Node(nodeA)
		self.nodeB = Node(nodeB)
		self.nodeC = Node(nodeC)
		
		self.nodeA.next = self.nodeB
		self.nodeB.next = self.nodeC
		
		self.nodeB.prev = self.nodeA
		self.nodeC.prev = self.nodeB
		
list1 = linkedList(1, 2, 3)

print("Nodes:", list1.nodeA.data, "-", list1.nodeB.data, "-", list1.nodeC.data)

print("2nd node's next node:", list1.nodeB.next.data)


print("2nd node's previous node:", list1.nodeB.prev.data)