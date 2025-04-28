# Create a linked list
#  10-->5-->16

class Node:
    def __init__(self, value):
        self.node = {
            "value": value,
            "next": None
        }

class myLinkedList:
    def __init__(self, value):
        self.head = {
            "value": value,
            "next": None
        }
        self.tail = self.head
        self.length = 1

    def append(self, value):
        self.tail["next"] = {
            "value": value,
            "next": None
        }
        self.tail = self.tail["next"]
        self.length += 1

    def prepend(self, value):
        newHead = {
            "value": value,
            "next": self.head
        }
        self.head = newHead
        self.length += 1

    def printList(self):
        currentNode = self.head
        while currentNode is not None:
            print(currentNode["value"])
            currentNode = currentNode["next"]

    def insert(self, index, value):
        # check parammeters
        if index >= self.length:
            return self.append(value)
        
        newNode = {
            "value": value,
            "next": None
        }

        leader = self.traverseToIndex(index-1)
        holdingPointer = leader["next"]
        leader["next"] = newNode
        newNode["next"] = holdingPointer
        self.length += 1


    def traverseToIndex(self, index):
        counter = 0
        currentNode = self.head
        while counter != index:
            currentNode = currentNode["next"]
            counter += 1
        return currentNode
    
    def delete(self, index):
        if index >= self.length:
            return False
        
        leader = self.traverseToIndex(index-1)
        unwantedNode = leader["next"]
        leader["next"] = unwantedNode["next"]
        self.length -= 1
        return True
    
    def reverse(self):
        if self.head is None:
            return None
        
        first = self.head
        self.tail = self.head
        second = first["next"]
        while second is not None:
            temp = second["next"]
            second["next"] = first
            first = second
            second = temp
        
        self.head["next"] = None
        self.head = first
        

LL = myLinkedList(10)
print("Initial")
LL.printList()

LL.append(5)
print("\nAppended 5")
LL.printList()

LL.append(16)
print("\nAppended 16")
LL.printList()

LL.prepend(1)
print("\nPrepended 1")
LL.printList()

LL.insert(2, 99)
print("\nInserted 99 at index 2")
LL.printList()

LL.delete(2)
print("\nDeleted index 2")
LL.printList()


LL.reverse()
print("\nReversed")
LL.printList()

LL.reverse()
print("\nReversed again")
LL.printList()