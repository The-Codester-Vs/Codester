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
    def delete(self,key):
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
    llist.push(1)
    llist.push(2)
    llist.delete(1)
    llist.printlist()

    

