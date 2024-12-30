class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Stack:
    def __init__(self):
        self.top=None

    def push(self,data):
        new_node=Node(data)
        new_node.next=self.top
        self.top=new_node

        print(f"pshed {data} to the stack")

    def pop(self):
        if self.is_empty():
            print("stack is empty cannot pop")
            return
        
        popped_data=self.top.data
        self.top=self.top.next
        return popped_data

    def peek(self):
        if self.is_empty():
            print("stack is empty")
            return None
        return self.top.data

    def is_empty(self):
        return self.top is None    

    def display(self):
        if self.is_empty():
            print("stack is empty")
            return
        current=self.top
        while current:
            print(current.data,end="->")
            current=current.next
        print("None")

s=Stack()
s.push(9)
s.push(6)
s.display()
s.pop()
s.display()
    
        
