class node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Linked_List:
    def __init__(self):
        self.start = None

    def inputlist(self,value):
        newnode = node(value)
        if self.start == None:
            self.start = newnode
        else:
            temp = self.start
            if temp.next != None:
                temp = temp.next
            temp.next = newnode
    
    def delete(self):
        if self.start == None:
            print("Your list is empty")
        else:
            # temp = self.start
            self.start = self.start.next

    def display(self):
        if self.start ==None:
            print('Your list is empty')
        else:
            temp = self.start
            while temp != None:
                print(temp.data)
                temp = temp.next
mystr = Linked_List()

