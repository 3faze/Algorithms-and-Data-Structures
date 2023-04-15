#reverse linked list
#1-2-3-4-NULL

class Node:
	def __init__(self, data):
		self.data = data
		self.next = Node
		self.prev = Node
		
nodeA = Node(1)
nodeB = Node(2)
nodeC = Node(3)
nodeD = Node(4)

nodeA.next = nodeB
nodeB.next = nodeC
nodeC.next = nodeD
nodeD.next = None

def reverse(head):
	prev = None
	curr = head
	next = None
	while curr is not None:
		next = curr.next
		curr.next = prev
		prev = curr
		curr = next
	return prev
	
tail = reverse(nodeA)	

curr = tail
while curr is not None:
	print(curr.data)
	curr = curr.next