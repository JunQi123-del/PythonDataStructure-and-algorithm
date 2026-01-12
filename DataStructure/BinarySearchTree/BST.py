class Node:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None
    
class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self,value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(self.root,value)
    
    def _insert(self,current,value):
        if value>current:
            if current.left is None:
                current.left = Node(value)
            else:
                self._insert(current.left,value)
        else:
            if current.right is None:
                current.right = Node(value)
            else:
                self._insert(current.right,value)
    
    def search(self,value):
        return self._search(self.root,value)
    
    def _search(self,current,value):
        if current is None:
            return False
        if value == current.key:
            return True
        if value < current.key:
            return self._search(current.left,value)
        else:
            return self._search(current.right,value)
    
    def delete(self,value):
        self.root = self._delete(self.root,value)

    def _delete(self,current,value):
        if current is None:
            return None
        
        if value <current.key:
            current.left = self._delete(current.left,value)
        elif value>current.key:
            current.right = self._delete(current.right,value)
        else:
            if current.left is None and current.right is None: # no children
                return None
            elif current.left is None:
                return current.right
            elif current.right is None:
                return current.right
            else:
                # node has both children so usees inorder traversal:
                # successor = the smallest value in the right sub tree
                #predecessor = the Biggest value in the left sub tree
                successor = self._find_predecessor(current.right)
                current.key = successor.key
                current.right = self._delete(current.right,successor.key)


    
    def _find_predecessor(self,current):
        #Find the biggest value in the right sub tree
        while current is not None and current.left is not None:
            current = current.left

        return current








            

        
