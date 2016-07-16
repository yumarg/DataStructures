class Node:
    def __init__(self, k):
        self.key = k
        self.prev = None
        self.next = None
    
    def getKey(self):
        return self.key
    
    def getPrev(self):
        return self.prev
    
    def getNext(self):
        return self.next
    
    def setPrev(self, newPrev):
        self.prev = newPrev
    
    def setNext(self, newNext):
        self.next = newNext

    def toString(self):
        string = "[Node with key: " + str(self.key) + "]"
        return string
    
class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def getHead(self):
        return self.head

    def getTail(self):
        return self.tail

    def empty(self):
        return (self.head == None and self.tail == None)
    
    def append(self, k):
        if (self.find(k) == "not there"):
            node = Node(k)
            if (self.empty()):
                self.head = node
            else:
                self.tail.setNext(node)
            self.tail = node      
    
    def prepend(self, k):
        if (self.find(k) == "not there"):
            node = Node(k)
            if (self.empty()):
                self.tail = node
            else:
                node.setNext(self.head)
            self.head = node      
    
    def insertAfter(self, k, kBefore):
        referenceNode = self.find(kBefore)
        if (referenceNode != "not there"):
            node = Node(k)
            if (self.tail == referenceNode):
                self.tail = node
            else:
                node.setNext(referenceNode.getNext())
            referenceNode.setNext(node)
        
    def delete(self, k):
        nodeToDelete = self.find(k)
        if (nodeToDelete != "not there"):
            if (self.head.getKey() == k):
                self.head = self.head.getNext()
            current = self.head.getNext()
            while (current != None):
                if (current.getNext() != None):
                    if (current.getNext().getKey() == k):
                        current.setNext(current.getNext().getNext())
                        if (self.tail.getKey() == k):
                            self.tail = current
                current = current.getNext()
    
    def find(self, k):
        current = self.head
        while (current != None):
            if (current.getKey() == k):
                return current
            else:
                current = current.getNext()
        if (current == None):
            return "not there"        

    def toString(self):
        string = "Singly Linked List with the following nodes:\n"
        current = self.head
        if (current == None):
            return "empty Singly Linked List"        
        while (current != None):
            if (self.head == current and self.tail == current):
                string += "\t - " + current.toString() + "\n"
            elif (self.head == current):
                string += "\t - [head]\t" + current.toString() + "\n"
            elif (self.tail == current):
                string += "\t - [tail]\t" + current.toString() + "\n"
            else:
                string += "\t - " + current.toString() + "\n"
            current = current.getNext()

        return string

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def empty(self):
        return (self.head == None and self.tail == None)

    def getHead(self):
        return self.head

    def getTail(self):
        return self.tail

    def append(self, k):
        if (self.find(k) == "not there"):
            node = Node(k)
            if (self.empty()):
                self.head = node
            else:
                node.setPrev(self.tail)
                self.tail.setNext(node)
            self.tail = node
        
    
    def prepend(self, k):
        if (self.find(k) == "not there"):
            node = Node(k)
            if (self.empty()):
                self.tail = node
            else:
                node.setNext(self.head)
                self.head.setPrev(node)
            self.head = node
    
    def insertAfter(self, k, kBefore):
        referenceNode = self.find(kBefore)
        if (referenceNode != "not there"):
            node = Node(k)
            if (self.tail == referenceNode):
                self.tail = node
            else:
                node.setNext(referenceNode.getNext())
                referenceNode.getNext().setPrev(node)
            node.setPrev(referenceNode)
            referenceNode.setNext(node)            

    def insertBefore(self, k, kAfter):
        referenceNode = self.find(kAfter)
        if (referenceNode != "not there"):
            node = Node(k)
            if (self.head == referenceNode):
                self.head = node
            else:
                node.setPrev(referenceNode.getPrev())
                referenceNode.getPrev().setNext(node)
            node.setNext(referenceNode)
            referenceNode.setPrev(node)

    def delete(self, k):
        nodeToDelete = self.find(k)
        if (nodeToDelete != "not there"):
            if (self.head.getKey() == k):
                if (self.tail == nodeToDelete):
                    self.head = None
                    self.tail = None
                else:
                    nodeToDelete.getNext().setPrev(None)                    
                    self.head = nodeToDelete.getNext()

            else:
                if (self.tail == nodeToDelete):
                    nodeToDelete.getPrev().setNext(None)                    
                    self.tail = nodeToDelete.getPrev()
                else:
                    nodeToDelete.getNext().setPrev(nodeToDelete.getPrev())
                    nodeToDelete.getPrev().setNext(nodeToDelete.getNext())
    
    def find(self, k):
        current = self.head
        while (current != None):
            if (current.getKey() == k):
                return current
            else:
                current = current.getNext()
        if (current == None):
            return "not there"

    def toString(self):
        string = "Doubly Linked List with the following nodes:\n"
        current = self.head
        if (current == None):
            return "empty Doubly Linked List"        
        while (current != None):
            if (self.head == current and self.tail == current):
                string += "\t - " + current.toString() + "\n"
            elif (self.head == current):
                string += "\t - [head]\t" + current.toString() + "\n"
            elif (self.tail == current):
                string += "\t - [tail]\t" + current.toString() + "\n"
            else:
                string += "\t - " + current.toString() + "\n"
            current = current.getNext()

        return string