# lets say we visit a website and we want to go back to the previous page
# we can use a stack to keep track of the pages we have visited

# This is an example 
# google.com -> facebook.com -> twitter.com


# can be built with arrays of linked lists
# using an array is a bad idea because we have to change index and size.
# using a linked list is better because we can add and remove elements easily
# but we have to keep track of the head and tail of the list
# but keep in mind about the cache locality reference for arrays which 
# results in better performance than linked lists

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0
    
    def peek(self):
        if self.top is None:
            return None
        return self.top        

    def push(self, value):
        # add a node to the top of stack
        newNode = Node(value)
        if self.length == 0:
            self.top = newNode
            self.bottom = newNode
        else:
            hold_top = self.top
            self.top = newNode
            self.bottom = hold_top
        self.length += 1
        return self
    
    def pop(self):
        # lets you remove from top of stack
        if self.length == 0:
            return None
        if self.length == 1:
            self.top = None
            self.bottom = None
        else:
            hold_top = self.top
            self.top = self.bottom
            self.bottom = hold_top.next
        self.length -= 1
        return hold_top.value

    def is_empty(self):
        # checks if stack is empty
        if self.length == 0:
            return True
        return False
    

myStack = Stack()
print(myStack.is_empty())  # Should print True
myStack.push("Discord")
print(myStack.peek().value)      # Should print "Discord"
myStack.push("Udemy")
print(myStack.peek().value) 
myStack.pop()
print(myStack.peek().value) 
myStack.push("Youtube")
print(myStack.peek().value) 
myStack.push("Google")
myStack.peek()
print(myStack.pop())
print(myStack.peek().value)  # Should print "Youtube"
print(myStack.is_empty())    # Should print False


    