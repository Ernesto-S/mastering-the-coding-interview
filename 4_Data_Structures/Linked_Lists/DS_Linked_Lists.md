# Linked List Notes
 
- A linked list is a list that is linked. There could be singly linked or doublelinked

- The initial element is called the head and the last element linked is called the tail. All linked list are ended with null value


## Why do you think linked lists are good?

- Initial thoughts is that linked list make for searching quicker and no memory conflicts.

- Instructures answer: Allows you to make inserts within a list easier since you don't have to worry about the indexing in a list.

| Action  | O(n) |
|---------|------|
| Prepend | O(1) |
| Append  | O(1) |
| Lookup  | O(n) |
| Insert  | O(n) |
| delete  | O(n) |

## What is a pointer?

A pointer is a reference to another place in memory. 

let obj1 = { a: Trure}
let obj2 = obj1

In this example obj2 is pointing to obj1