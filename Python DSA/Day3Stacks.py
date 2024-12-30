class Stack:
    def __init__(self):
        self.stack=[]

    def push(self,item):
        self.stack += [item]
        print(f"pushed:{item}")

    def pop(self):
        if self.is_empty():
            print("Stack is_empty Cannot pop")
            return None
        item=self.stack[-1]
        self.stack=self.stack[:-1]
        print(f"Popped:{item}")
        return item

    def peek(self):
        if self.is_empty():
            print("Stack is_empty")
        print(f"Peek is:{self.stack[-1]}")
        return self.stack[-1]
    def is_empty(self):
        return len(self.stack)==0
    def size(self):
        count=0
        for i in self.stack:
            count += 1
        print(f"size:{count}")
        return count
stack=Stack()
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(6)
stack.push(9)
stack.pop()
stack.pop()
stack.peek()
stack.is_empty()
stack.size()
