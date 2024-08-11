class TreeNode:
    def __init__(self, val=None):

        self.val = val #value of the node (cargo)
        self.left = None
        self.right = None

    def getValue(self): #returns value
        return self.val

    def setValue(self, newVal): #sets value
        self.val = newVal

    def getLeftChild(self): #gets the value left of then node
        return self.left

    def setLeftChild(self, newLeft): #sets the valyue left of the node
        self.left = newLeft

    def getRightChild(self): #gets the value right of the node
        return self.right

    def setRightChild(self, newRight): #sets the value right of the node
        self.right = newRight

class BinarySearchTree:
    def __init__(self, limit=None):
        self.root = None
        self.limit = limit #limit is passed during tree creation

    def search(self, value): #public facing search method
        return self._search(self.root, value)

    def _search(self, node, value): #_ indicates this is a private method for the class. during search, a node and a value is passed in.
        if node is None:
            return False
        if node.getValue() == value: #if node's value is what's being searched, return tru
            return True
        elif value < node.getValue(): #check whether to go left or right in tree (recusively)
            return self._search(node.getLeftChild(), value) 
        else:
            return self._search(node.getRightChild(), value)

    def insert(self, value):
        if self.limit is not None and len(self.traverse()) >= self.limit: #check whether there is room to insert a new value into tree
            print("Tree is full. Cannot insert more nodes.")
            return
        self.root = self._insert(self.root, value)

    def _insert(self, node, value): #insert node/value into tree
        if node is None:
            return TreeNode(value)
        if value <= node.getValue(): #if value is less than node, go left child
            node.setLeftChild(self._insert(node.getLeftChild(), value))
        else: #else, go right child
            node.setRightChild(self._insert(node.getRightChild(), value))
        return node

    #I was unable to implement the delete function. below is how far I got.
    """def delete(self, value): 
        self.root = self._delete(self.root, value)

    def _delete(self, node, value): #delete node/value
        if node is None: #don't delete if node isn't found
            return node
        if value < node.getValue(): #if the value is less than current node value, call _delete method (recursively) on left child
            node.setLeftChild(self._delete(node.getLeftChild(), value))
        elif value > node.getValue(): #likewise, if the value is greater call on right child 
            node.setRightChild(self._delete(node.getRightChild(), value))
        """
    #Thankfully this does not impact the rest of question 3.

    def traverse(self): #traverse puts values of tree into list
        result = []
        self._traverse(self.root, result)
        return result

    def _traverse(self, node, result): #in order traversal
        if node is not None: #recursively calls _traverse function to find nodes until leaf nodes are reached
            self._traverse(node.getLeftChild(), result)
            result.append(node.getValue())
            self._traverse(node.getRightChild(), result)

    def printTree(self): #prints the tree
        print("Binary Search Tree:")
        self._printTree(self.root, 0)

    def _printTree(self, node, spacing): #private method takes in node, and spacing (spcaing depending on the level the node's position in the tree is).
        if node is not None:
            spacing += 1
            self._printTree(node.getRightChild(), spacing) 
            print("   " * spacing + str(node.getValue())) # makes sure there's the correct amount of spacing between nodes. prints value as string. "  " * int outputs string 3 times 
            self._printTree(node.getLeftChild(), spacing)

