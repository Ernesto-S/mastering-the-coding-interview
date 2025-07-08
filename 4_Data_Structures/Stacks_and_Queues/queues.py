# Create queue data structure

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def peek(self):
        # Returns the first item in queue
        if self.first is None:
            return None
        return self.first.value

    def enqueue(self, value):
        # Adds to queue
        newNode = Node(value)
        if self.length == 0:
            self.first = newNode
            self.last = newNode
        else:
            self.last.next = newNode
            self.last = newNode
        self.length += 1
        return self

    def dequeue(self):
        # Removed from the front of the Queue
        if self.length == 0:
            return None
        hold_first = self.first
        if self.length == 1:
            self.first = None
            self.last = None
        else:
            self.first = hold_first.next
        self.length -= 1
        return hold_first.value

    def is_empty(self):
        if self.length == 0:
            return True
        else:
            return False
    
    def __str__(self):
        items = []
        current = self.first
        while current:
            items.append(str(current.value))
            current = current.next
        return "Queue: [" + ", ".join(items) + "]"
    
myQueue = Queue()
myQueue.enqueue("Walas")
myQueue.enqueue("Adalberto")
myQueue.enqueue("Chaparra")
print(myQueue.peek())
print(myQueue)

while myQueue.length != 0:
    print(myQueue)
    myQueue.dequeue()
    
print(myQueue.is_empty())