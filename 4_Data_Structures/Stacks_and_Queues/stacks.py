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

class Stack:
    def __init__(self):
        self.stack = []
    
    