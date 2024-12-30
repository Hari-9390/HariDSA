class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None

class DoubleLinkedList:
    def __init__(self):
        self.head=None

    def append(self,data):
        new_node=Node(data)
        if not self.head:
            self.head=new_node
            return
        last=self.head
        while last.next:
            last=last.next
        last.next=new_node
        new_node.prev=last

    def prepend(self,data):
        new_node=Node(data)

        if not self.head:
            self.head=new_node
            return
        new_node.next=self.head
        self.head.prev=new_node
        self.head=new_node
    def print_list(self):
        current=self.head
        while current:
            print(current.data,end="->")
            current=current.next
        print()

dl=DoubleLinkedList()
dl.append(9)
dl.append(6)
dl.append(0)
dl.print_list()

        
