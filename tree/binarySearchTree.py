# Binary search tree

class Tree:
    # EMpty node has value, left, right = None
    def __init__(self, initial = None):
      # creating an empty node or leaf node depending on the initial value
        self.value = initial
        if self.value:
            self.left = Tree()
            self.right = Tree()
        else:
            self.left = None
            self.right = None
        return
    
    def isEmpty(self):
    # to check if the node has value empty
        return(self.value == None)       
   
    def inorder(self):
        # inorder traversal
        if self.isEmpty():
            return([])
        else:
            return(self.left.inorder() +
                   [self.value] +
                   self.right.inorder())

    def __str__(self):
        # printing the whole tree (inorder traversal)
        return(str(self.inorder()))

    def find(self,v):
        # finding a value v in the tree
        if self.isEmpty():
            return(False)
        elif self.value == v:
            return(True)
        elif self.value > v:
            return(self.left.find(v))
        else:
            return(self.right.find(v))
 
    def minimumValue(self):
        # return the minimum value in the tree
        if self.isEmpty():
            return()
        if self.left.isEmpty():
            return(self.value)
        else:
            return(self.left.minimumValue())
    
    def maximumValue(self):
        # return the maximum value in the tree
        if self.isEmpty():
            return()
        if self.right.isEmpty():
            return(self.value)
        else:
            return(self.right.maximumValue())  

    def insert(self,v):
        # insert the value v in the BST
        if self.isEmpty():
            self.value = v
            self.left = Tree()
            self.right = Tree()
        if self.value == v:
            return
        if self.value < v:
            self.right.insert(v)
            return
        if self.value > v:
            self.left.insert(v)
            return
    
    def isLeaf(self):
        # returns True if the node is a leaf node
        if self.left == None and self.right == None:
            return(True)
        else:
            return(False)

    def makeEmpty(self):
        # it will make the node empty, that is it will set value, left pointer, right pointer to None
        self.value = None
        self.left = None
        self.right = None
        return
    
    def copyRight(self):
        # copying the right value to current node
        self.value = self.right.value
        self.left= self.right.left
        self.right = self.right.right
        return
    
    def delete(self,v):
        # deleting the value v in the BST
        if self.isEmpty():
            return
        if self.value < v:
            return(self.right.delete(v))
        if self.value > v:
            return(self.left.delete(v))
        if self.value == v: 
            if self.isLeaf():
                self.makeEmpty()
            elif self.left.isEmpty():
                self.copyRight()
            else:
                self.value = self.left.maximumValue()
                self.left.delete(self.left.maximumValue())
            return                                                       

