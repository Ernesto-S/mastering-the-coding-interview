# Create a linked list
#  10-->5-->16

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


LL = myLinkedList(10)
print("\nInitial Head", LL.head)
print("Initial Tail", LL.tail)
print("Initial Length", LL.length)

LL.append(5)
print("\nAppended Head", LL.head)
print("Appended Tail", LL.tail)
print("Appended length", LL.length)

LL.append(16)
print("\nAppended Head", LL.head)
print("Appended Tail", LL.tail)
print("Appended length", LL.length)

LL.prepend(1)
print("Prepended Head", LL.head)
print("Prepended Tail", LL.tail)
print("Prepended length", LL.length, "\n")


