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
        if value == current.value:
            return True
        if value < current.value:
            return self._search(current.left,value)
        else:
            return self._search(current.right,value)
    
    def delete(self,value):
        self.root = self._delete(self.root,value)

    def _delete(self,current,value):
        if current is None:
            return None
        if current.key > value:
            current.left = 