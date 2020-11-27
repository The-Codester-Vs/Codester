class node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class linked_list:
    def __init__(self):
        self.head = None
        
    def insert(self,value):
        element = node(value)
        
        if self.head == None:
            self.head = element
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = element
    
    def display(self):
        temp = self.head
        while temp != None:
            print(temp.data)
            temp = temp.next
        
    
my = linked_list()
my.insert(1)
my.insert(2)
my.display()