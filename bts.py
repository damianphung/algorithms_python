#https://www.tutorialspoint.com/python/python_binary_search_tree.htm

class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data

    def search(self, data):
        """
                 6
        1  2  4    5  6  9
        """
        if ( data < self.data ):
            if ( self.left is None ):
                self.left = Node(data)
            else:
                self.left.search(data)
        else:
            # ( data > self.data )
            self.right.search(data)

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data
     
    

        if self.data < data:
            return self.left.search(data) 
        else:
            return self.right.search(data)
