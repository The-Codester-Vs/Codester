class node:
	def __init__(self,data):
		self.data = data
		self.next = None

class linked_list:
	def __init__(self):
		self.head = None

	def push(self,new_data):
		new_node = node(new_data)
		new_node.next = self.head
		self.head = new_node

	def insertAfter(self,prev_node,new_data):
		if prev_node is None:
			print("Previous node is empty")
			return

		new_node = node(new_data)
		new_node.next = prev_node.next
		prev_node.next = new_node		

	def append(self,new_data):
		new_node = node(new_data)
		if self.head is None:
			self.head = new_node
			return

		last = self.head
		while(last.next):
			last = last.next
		last.next = new_node

	def printlist(self):
		temp = self.head	
		while (temp):
			print(temp.data)
			temp = temp.next
if __name__ == '__main__':
	
	llist = linked_list()
	llist.append(1)
	llist.append(2)
	llist.push(0)
	llist.insertAfter(llist.head.next,12)
	# llist.delete()
	llist.printlist()	


