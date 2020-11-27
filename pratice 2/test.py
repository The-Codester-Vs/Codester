class node:
    def __init__(self,data):
        self.data = data
        self.next = None

class linked:
    def __init__(self):
        self.head = None
    
    def push(self,new_data):
        new_node = node(new_data)
        new_node.next = self.head
        self.head = new_node
    
    def insertAfter(self,prev_node,new_data):
        if prev_node is None:
            print("There is no previous node")
            return
        
        new_node = node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node
    
    def append(self,new_data):
        new_node = node(new_data)
        if self.head is None:
            self.head = new_node
            return
        
        value = self.head
        while(value.next):
            value = value.next
        value.next = new_node
    
    def delete_element(self,key):
        temp = self.head
        if (temp is not  None ) :
            if (temp.data == key) :
                self.head = temp.next
                temp = None
                return
            
            
        while (temp is not None):
            if (temp.data == key):
                break
            prev  = temp
            temp = temp.next
            
        if temp == None:
            return
        
        prev.next = temp.next
        temp = None
    
    def getcount(self):
        temp = self.head
        count = 0
        while (temp):
            count += 1
            temp = temp.next
        return count  
    
    def search(self,x):
        current = self.head
        
        while current!= None:
            if current.data == x:
                return True
            
            current = current.next
        return False 
        
        
    # printing the linked list
    def printlist(self):
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.next
            
          
if __name__ == '__main__':
    llist = linked()
    # appending the elements
    llist.append(2)
    llist.append(3)
    llist.append(4)
    # pushing 1 at first index
    llist.push(1)
    llist.insertAfter(llist.head,1.5) # inserting new element between 1 and 2
    llist.printlist()
    print("Total numbers of nodes are:",llist.getcount())
    
    # n = int(input("Enter the number which do you want search: "))
    if llist.search(n):
        print("Your value is in the list")
    else:
        print("Your value is not in the list") 
    
   
                 