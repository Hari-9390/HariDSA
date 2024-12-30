class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class SingleLinkedList:
    def __init__(self):
        self.head=None
    
    def insert(self,data):
        new_node=Node(data)
        if not self.head:
            self.head=new_node
            return
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=new_node

    def delete(self,key):
        temp=self.head
        if temp and temp.data == key:
            self.head=temp.next
            temp=None
            return
        
        prev=None
        
        while temp and temp.data!=key:
            prev=temp
            temp=temp.next
        
        if not temp:
            print("Node not found")
            return
        
        prev.next=temp.next

        temp=None

    def print_list(self):
        temp=self.head
        while temp:
            print(temp.data,end='->')
            temp=temp.next
        print("None")

sll=SingleLinkedList()
sll.insert(10)
sll.insert(11)
sll.insert(12)
sll.insert(13)
sll.insert(14)
sll.insert(15)
sll.insert(16)
sll.insert(17)
sll.insert(18)
sll.insert(19)
sll.print_list()
sll.delete(11)
sll.delete(13)
sll.delete(15)
sll.delete(17)
sll.delete(19)
sll.print_list()
