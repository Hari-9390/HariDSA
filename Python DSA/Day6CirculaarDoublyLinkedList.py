class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None

class CircularDoubleLinkedList:
    def __init__(self):
        self.head=None
    def insert(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            self.head.next=self.head
            self.head.prev=self.head

        else:
            tail=self.head.prev
            tail.next=new_node
            new_node.next=self.head
            new_node.prev=tail
            self.head.prev=new_node

    def delete(self,key):
        if self.head is None:
            print("List is empty")
            return
        current=self.head
        while True:
            if current.data==key:
                self.head=None
            else:
                current.prev.next=current.next
                current.next.prev=current.prev
                if current==self.head:
                    self.head=current.next
            print(f"Node has data{key} deleted")
            return

         current=current.next
         if current==self.head:
             break
        print(f"node with data{key} not found")


    def display(self):
        if self.head is None:
            print("List is empty")
            return
        current=self.head
        while current:
            print(current.data,end='->')
            current=current.next
            if current==self.head:
                break

dcl=CircularDoublyLinkedList()
dcl.insert(10)
dcl.insert(12)
dcl.insert(14)
dcl.insert(16)
dcl.insert(19)
dcl.display()
dcl.delete(10)
dcl.delete(17)
dcl.delete(18)
dcl.delete(16)











        
