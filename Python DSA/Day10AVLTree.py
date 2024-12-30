class Node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.key=key
        self.height=1

class AVLTree:
    def height(self,node):
        if node is None:
            return 0
        return node.height
    def get_balance(self,node):
        if node is None:
            return 0
        return self.get_height(node.left)-self.get_height(node.left)
    
    def get_max(self,x,y):
        if x>y:
            return x
        else:
            return y

    def right_rotation(self,x):
        y=x.left
        y1=x.right

        y.right=x
        x.left=y1
        
        x.height=1+self.get_max(self.get_height(x.left),self.get_height(x.right))
        y.height=1+self.get_max(self.get_height(y.left),self.get_height(y.right))

        return y

    def left_rotation(self,y):
        x=y.right
        y1=y.left

        x.right=y
        y.left=y1
        
        x.height=1+self.get_max(self.get_height(y.left),self.get_height(y.right))
        y.height=1+self.get_max(self.get_height(x.left),self.get_height(x.right))

        return x
    

    
 
