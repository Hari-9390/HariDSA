#Linked Lists

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class LinkedList:
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
        
        if temp and temp.data==key:
            self.head=temp.next
            temp=None
            return
        
        while temp and temp.data!=key:
            temp=temp.next
            
        if not temp:
            print("Node not found")
            return
        
        temp=None
        
    def print_list(self):
        temp=self.head
        while temp:
            print(temp.data,end="->")
            temp=temp.next
        print("None")
        
ll=LinkedList()

ll.insert_end(5)
ll.insert_end(10)
ll.insert_end(15)

print("Linked List after insertion:")
ll.print_list()

ll.delete_node(5)
ll.print_list()




