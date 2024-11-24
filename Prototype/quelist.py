class Node:
    def __init__(self, que):
        self.que = que
        self.next = None
        self.prev = None

#Doubly Linked List Implementation
class QueList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def add(self, que):
        self.length+=1
        if self.head:
            self.tail.next = Node(que)
            self.tail.next.prev = self.tail
            self.tail = self.tail.next
        else:
            self.head = Node(que)
            self.tail = self.head