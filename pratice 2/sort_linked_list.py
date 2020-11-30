class node:
    def __init__(self,data):
        self.data = data
        self.next = None

class link:
    def __init__(self):
        self.head = None
    
    def append(self,new_data):
        new_node = node(new_data)
        if self.head == None:
            self.head = new_node
        else:
            temp = self.head
            while(temp.next):
                temp = temp.next
            temp.next = new_node
            
    def sort(self):
        current = self.head
        index = None
        
        if (self.head == None):
            return
        else:
            while(current != None):
                index = current.next
                while (index != None):
                    if (current.data > index.data):
                        temp = current.data
                        current.data = index.data
                        index.data = temp
                    index = index.next
                current = current.next    
                
    def display(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next           
                    

if __name__ == '__main__':
    Sort = link()
    Sort.append(7)
    Sort.append(5)
    Sort.append(3)
    Sort.append(9)
    Sort.sort()
    Sort.display()