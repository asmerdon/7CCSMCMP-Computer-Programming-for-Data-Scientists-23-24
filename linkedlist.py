class ListNode:
    def __init__(self, data=None): #initialise 
        self.data = data
        self.next = None

    def getData(self): #return data
        return self.data

    def setData(self, data): #set data
        self.data = data

    def getNext(self): #return next node
        return self.next

    def setNext(self, next_node): #set next node
        self.next = next_node

    def __str__(self): #return string representation of the node (overwrites default str implemenation)
        return str(self.data)


class LinkedList:
    def __init__(self, limit=None): #initialise
        self.firstNode = None
        self.sizeLimit = limit

    def is_empty(self): #check if empty
        return self.firstNode is None

    def is_full(self): #check if linked list is full
        if self.sizeLimit is None:
            return False
        count = 0
        current = self.firstNode
        while current: #iterates through linked list node by node
            count += 1
            current = current.getNext()
        return count >= self.sizeLimit #return true or false if linked list is full

    def __str__(self): #return string representation of the linked list (overwrites default str implemenation)
        if self.is_empty():
            return "Empty List"
        else:
            elements = [] #define element list
            current = self.firstNode
            while current:
                elements.append(str(current)) #append current node to list as str
                current = current.getNext() #gets next node
            return elements
        
    def search(self, value): #searches linked list for value
        current = self.firstNode
        while current:
            if current.getData() == value: #return true if value is found
                return True
            current = current.getNext() #get next node
        return False

    def insert(self, data):
        if self.is_full():
         print("Cannot insert node.")
        else:
            newNode = ListNode(data)
            if self.firstNode is None:  #if the list is empty new node becomes the first node
                self.firstNode = newNode
            else:
                current = self.firstNode
                while current.getNext() is not None:  #iterate until the last node
                    current = current.getNext()
                current.setNext(newNode)  #insert the new node at the end

    def delete(self, data):
        current = self.firstNode #get first node
        previous = None
        found = False
        while not found and current is not None: #work through list node by node until value is found
            if current.getData() == data:
                found = True
            else:
                previous = current
                current = current.getNext()
        if found:
            if previous is None: #if node to be deleted is the first in list
                self.firstNode = current.getNext() #set first node in list to be next (second) node
            else:
                previous.setNext(current.getNext()) #otherwise set the previous node's next pointer to node after (skipping over current node)

    def traverse(self):
        elements = [] #declare list
        current = self.firstNode #start at fist node
        while current: #iterate through linked list
            elements.append(current.getData()) #add to list
            current = current.getNext()
        return elements
