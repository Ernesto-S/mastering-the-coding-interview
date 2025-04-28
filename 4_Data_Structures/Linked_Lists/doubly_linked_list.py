
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def prepend(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def delete(self, node):
        if node.prev:
            node.prev.next = node.next
        else:
            self.head = node.next

        if node.next:
            node.next.prev = node.prev
        else:
            self.tail = node.prev
    
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")

    def print_reverse(self):
        current = self.tail
        while current:
            print(current.data, end=" <-> ")
            current = current.prev
        print("None")
    
    def find(self, data):
        current = self.head
        while current:
            if current.data == data:
                return current
            current = current.next
        return None

    def insert_after(self, prev_node, data):
        if not prev_node:
            print("Previous node cannot be None")
            return

        new_node = Node(data)
        new_node.next = prev_node.next
        new_node.prev = prev_node

        if prev_node.next:
            prev_node.next.prev = new_node
        else:
            self.tail = new_node

        prev_node.next = new_node
        print(f"Inserted {data} after {prev_node.data}")

    def insert_before(self, next_node, data):
        if not next_node:
            print("Next node cannot be None")
            return

        new_node = Node(data)
        new_node.prev = next_node.prev
        new_node.next = next_node

        if next_node.prev:
            next_node.prev.next = new_node
        else:
            self.head = new_node

        next_node.prev = new_node
        print(f"Inserted {data} before {next_node.data}")

    def clear(self):
        self.head = None
        self.tail = None
        print("List cleared")

DL = DoublyLinkedList()
DL.append(1)
DL.append(2)
DL.append(3)
DL.prepend(0)
DL.print_list()  # Output: 0 <-> 1 <-> 2 <-> 3 <-> None
DL.print_reverse()  # Output: 3 <-> 2 <-> 1 <-> 0 <-> None
DL.insert_after(DL.head.next, 1.5)  # Insert 1.5 after 1
DL.print_list()  # Output: 0 <-> 1 <-> 1.5 <-> 2 <-> 3 <-> None
DL.insert_before(DL.tail, 2.5)  # Insert 2.5 before 3
DL.print_list()  # Output: 0 <-> 1 <-> 1.5 <-> 2 <-> 2.5 <-> 3 <-> None
DL.delete(DL.head.next)  # Delete node with value 1.5
DL.print_list()  # Output: 0 <-> 1 <-> 2 <-> 2.5 <-> 3 <-> None
DL.clear()  # Clear the list
DL.print_list()  # Output: None
