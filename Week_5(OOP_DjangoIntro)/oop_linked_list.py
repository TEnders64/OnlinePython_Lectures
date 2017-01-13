class SinglyLinkedListNode(object):
	def __init__(self, val):
		self.val = val
		self.next = None

class SinglyLinkedList(object):
	def __init__(self):
		self.head = None

	def addFront(self, val):
		#if list is empty (head is None)
		if not self.head:
			self.head = SinglyLinkedListNode(val)
		else:
			#create a new node
			#do something to save our old head node
			#make our new node's Next pointer point to the old head node
			#make the new node be the head node
			node = SinglyLinkedListNode(val) #instantiates a new node
			node.next = self.head
			self.head = node

	def addBefore(self, val, next_val):
		runner = self.head
		if not runner:
			raise NoHeadError('There is nothing in the list')
		elif not runner.next:
			if runner.val == next_val:
				addFront(val)
			else:
				raise NextValNotInListError('The next val was not found')
		else:
			while runner.next:
				if runner.next.val == next_val:
					new_node = SinglyLinkedListNode(val)
					rest_of_list = runner.next
					runner.next = new_node
					new_node.next = rest_of_list
					return True
				else:
					runner = runner.next
			raise NextValNotInListError('The next val was not found')



our_list = SinglyLinkedList()
our_list.addFront(2)
our_list.addFront(3)


print our_list.head.val
