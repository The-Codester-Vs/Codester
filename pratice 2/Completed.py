class node:
    def __init__(self,data):
        self.data = data
        self.next = None

class linked:
    def __init__(self):
        self.head = None
    
    # pushing node at 1st
    def push(self,new_data):
        new_node = node(new_data)
        new_node.next = self.head
        self.head = new_node
    
    # inserting the node before aur after the head node
    def insertAfter(self,prev_node,new_data):
        if prev_node is None:
            print("There is no previous node")
            return
        
        new_node = node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node
    
    # adding the element into the list
    def append(self,new_data):
        new_node = node(new_data)
        if self.head is None:
            self.head = new_node
            return
        
        value = self.head
        while(value.next):
            value = value.next
        value.next = new_node
    
    # deleting the element 
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
    
    # counting the total numbers of node
    def getcount(self):
        temp = self.head
        count = 0
        while (temp):
            count += 1
            temp = temp.next
        return count  
    
    # searching the node in the linked list
    def search(self,x):
        current = self.head
        
        while current!= None:
            if current.data == x:
                return True
            
            current = current.next
        return False
    
    # sortting the linked list in incresing order 
    def sort(self):
        current = self.head
        index = None
        
        if (self.head == None):
            return
        else:
            while(current != None):
                index = current.next
                while(index != None):
                    if (current.data > index.data):
                        temp = current.data
                        current.data = index.data
                        index.data = temp
                    index = index.next
                current = current.next
                        
                                 
        
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
    # pushing at first index
    llist.push(1)
    llist.push(6)
    # inserting the element before and after the head node
    llist.insertAfter(llist.head,1.5) # inserting new element before 2 and
    llist.delete_element(3)
    llist.printlist()
    
    print("Sorted List:")
    llist.sort()# sorting the list in incresing order
    llist.printlist()
    
    print("--------------------------------------------------------")
    
    print("Total numbers of nodes are:",llist.getcount())
    # n = int(input("Enter the number which do you want search: "))
    if llist.search(3):
        print("Your value is in the list")
    else:
        print("Your value is not in the list") 
    
   
                 