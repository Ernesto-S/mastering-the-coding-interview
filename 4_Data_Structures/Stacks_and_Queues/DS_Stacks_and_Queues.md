# Stacks and Queues 

These are very similar. they are linear data structures. Where only one data can be accessed at a time. Typically deal with items in the beginning or end. These are beneficial when trying to limit the options a developer has. 

## Stacks

LIFO Last in First Out

| Action | O(n) |
|--------|------|
| lookup | O(n) |
|  pop   | O(1) |
|  push  | O(1) |
|  peek  | O(1) |

Example of use:
- Browser history
- Undo/redo option
- Think of stacked plates. The top plate is taken first and plates continue to stack on the top. 

## Queue

FIFO First in First out

| Action  | O(n) |
|---------|------|
| lookup  | O(n) |
| enqueue | O(1) |
| dequeue | O(1) |
|  peek   | O(1) |

Example of use:
- Think of a line to a roller coaster. The people queue in line but the first one in line goes first
- anything with a wait list
- Ride share apps
- Using printers 

## Stacks and Queues in JavaScript Programming Language. 

JavaScript is a single threaded language that can be NON blocking. It only has a
"Call Stack" and a "Memory Heap"

Memory Heap is the allowable space of memory. Where variables are stored

Call stack is a Queue that follows first in first out sequence for the program.

The website "Stack Overflow" comes from the Call Stack exceeding the space in the 
Call Stack. One way to create a Stack Overflow event is recursion. Where a function
calls itself within the 

Javascript is synchronous programming language. In order to not block the single thread language it can be made to be Asynchronous by creating an event loop that can run the steps in the queues. If there is ever a step that takes longer it will start it, but skip to the next line in order to output the value. 