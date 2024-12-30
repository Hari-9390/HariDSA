class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None

    def append(self,data):
        new_node=Node(data)
        if not self.head:
            self.head=new_node
            return
        current=self.head
        while current.next:
            current=current.next
        current.next=new_node
    def delete(self,value):
        if not self.head:
            return
        if self.head.data==value:
            self.head=self.head.next
            return
        current=self.head
        while current.next and current.next.data!=value:
            current=current.next
        if current.next:
            current.next=current.next.next

    def display(self):
        current=self.head
        while current:
            print(current.data,end="->")
            current=current.next
        print("None")

    def reverse(self):
        prev=None
        current=self.head
        while current:
            next_node=current.next
            current.next=prev
            prev=current
            current=next_node
        self.head=prev

    def find_middle(self):
        first=last=self.head
        while last and last.next:
            first=first.next
            last=last.next.next
        return first.data if first else None

sl=LinkedList()
sl.append(3)
sl.append(5)
sl.append(7)
sl.append(8)
sl.append(9)
sl.display()
sl.reverse()
sl.display()
sl.find_middle()
sl.display()

