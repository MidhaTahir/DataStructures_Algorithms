class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self,newNode):
        if self.head is None:
            self.head = newNode

        else:
        
            lastNode = self.head
            while True:
                if lastNode.next is None: 
                    break
                lastNode = lastNode.next 
            lastNode.next = newNode
    
    def addhead(self,newNode):
        tempNode = self.head
        self.head =  newNode
        self.head.next = tempNode
        del tempNode

    def listLength(self):
        currentNode = self.head
        length = 0
        while currentNode is not None:
            length += 1
            currentNode = currentNode.next
        return length

    
    def insertAt(self,newNode,position):
        if position < 0 or position > self.listLength():
            print("Invalid Position")
        if position is 0:
            self.addhead(newNode)
            return 
        currentNode = self.head
        currentPosition = 0
        while True:
            if currentPosition == position:
                previousNode.next = newNode
                newNode.next = currentNode
                break
            previousNode = currentNode
            currentNode = currentNode.next
            currentPosition += 1

        

    def deleteEnd(self):
        lastNode = self.head
        while lastNode.next is not None:
            previousNode = lastNode
            lastNode = lastNode.next
        if self.listLength() is 1:
            self.head = None
        else:
            previousNode.next = None
        

        

    def deleteAt(self,position):
        if position < 0 or position >= self.listLength():
            print("Invalid position")
            return
        if self.listLength() is 0: #empty list
            if position is 0: #head node
                self.deleteEnd()
                return 
            
            currentNode = self.head
            currentPosition = 0
            while True:
                if currentPosition == position:
                    previousNode.next = currentNode.next
                    break
                previousNode = currentNode
                currentNode = currentNode.next
                currentPosition += 1

    def printList(self):
        if self.head is None:
            print("Linked List is empty")
            return
        currentNode = self.head
        while(True):
            if currentNode is None:
                break
            print(currentNode.data)
            currentNode = currentNode.next
            
        


firstNode = Node(10)
linkedList = LinkedList()
linkedList.addhead(firstNode)

secondNode = Node(20)
linkedList.append(secondNode)

thirdNode = Node("Mathew")
linkedList.append(thirdNode)

fourthNode = Node("Mids")
linkedList.addhead(fourthNode)

fifthNode = Node("Barth")
linkedList.insertAt(fifthNode,1) 

linkedList.deleteEnd()
linkedList.deleteEnd()
linkedList.deleteEnd()
linkedList.deleteAt(0)

linkedList.printList()