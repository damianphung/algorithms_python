#https://www.tutorialspoint.com/python/python_binary_search_tree.htm

import tensorflow as tf

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
                print("cannot find {}".format(data))
            else:
                self.left.search(data)
        elif ( data > self.data ):
            if ( self.right is None ):
                print("cannot find {}".format(data))
            else:
                self.right.search(data)
        else:
            # Found it
            print ("Found {}".format(data))

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

    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.data)
        if self.right:
            self.right.PrintTree()

def main():
    root = Node(6)
    root.insert(7)
    root.insert(2)
    root.insert(100)
    root.insert(1)
    root.insert(8)
    root.insert(13)
    root.insert(15)
    root.PrintTree()
    root.search(2)


main()