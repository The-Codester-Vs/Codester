class node:
    def __init__(self,data):
        self.data = data
        self.next = None

class linked:
    def __init__(self):
        self.head = None

    def append(self,new_data):
        new_node = node(new_data)
        if self.head == None:
            self.head = new_node
            return
        
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def delete_element(self,key):
        temp = self.head

        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                temp = None
                return


        while(temp is not None):
            if temp.data == key:
                break
            prev= temp
            temp = temp .next

        if temp == None:
            return

        prev.next = temp.next
        temp = None

    def printlist(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next
if __name__ == '__main__':
    
    llist = linked()
    llist.append(1)
    llist.append(2)
    llist.append(3)
    # llist.delete_element(1)
    llist.printlist()

    

