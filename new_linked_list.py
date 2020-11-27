class node:# !making class here
    def __init__(self,data):
        self.data = data
        self.next = None

class new_linked_list:# !making another class here
    def __init__(self):
          self.head = None

    def insert(self,val):
        new_node = node(val)
        if self.head == None:
            self.head = new_node
        else:
            temp = self.head
            if temp.next!= None:
                temp = temp.next
            temp.next = new_node

    def display(self):
        if self.head  == None:
            print("Your list is empty")
        else:
            temp = self.head
            while temp != None:
                print(temp.data)
                temp = temp.next

    def delete(self):
        if self.head == None:
            print("your linked is empty") 
        else:
            self.head = self.head.next

mystr = new_linked_list()#calling class here
# !calling functions form the class 
mystr.insert(12) 
mystr.insert(122)
mystr.insert(2)
mystr.display()

