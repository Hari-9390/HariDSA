class Node:
    def __init__(self,value):
        self.left=None
        self.right=None
        self.value=value

    def insert(self,value):
        if value<self.value:
            if self.left is None:
                self.left=Node(value)
            else:
                self.left.insert(value)

        elif value>self.value:
            if self.right is None:
                self.right=Node(value)
            else:
                self.right.insert(value)

    def inorder(self):
        if self.left:
            self.left.inorder()
        print(self.value,end="->")
        if self.right:
            self.right.inorder()


    def preorder(self):
        print(self.value,end="->")
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()

    def postorder(self):
        if self.left:
            self.left.postorder()
        if self.right:
            self.right.postorder()
        print(self.value,end="->")

    def search(self,value):
        if value==self.value:
            return 1
        elif value<self.value and self.left:
            return self.left.search(value)
        elif value>self.value and self.right:
            return self.right.search(value)
        return False
    
    def min_value_node(self):
        current=self
        while current.left:
            current=current.left
        return current.value
    
    def max_value_node(self):
        current=self
        while current.right:
            current=current.right
        return current.value
    
    def delete(self,value):
        if value<self.value:
            if self.left:
                self.left=self.left.delete(value)
        elif value>self.value:
            if self.right:
                self.right=self.right.delete(value)
        else:
            if not self.left:
                return self.right
            elif not self.right:
                return self.left
            min_value=self.right.min_value_node().value
            self.value=min_value
            self.right=self.left.delete(value)
        return self
            
ab=Node(5)
ab.insert(2)
ab.insert(3)
ab.insert(4)
ab.insert(5)
ab.insert(6)
ab.insert(7)
ab.inorder()
print()
ab.preorder()
print()
ab.postorder()
print(ab.search(9))
print(ab.max_value_node())
print(ab.min_value_node())
ab.delete(4)
ab.postorder()



