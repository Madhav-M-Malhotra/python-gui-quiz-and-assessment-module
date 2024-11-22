class Node:
    def __init__(self, que : int):
        self.que = que
        self.next = None
        self.prev = None

#Doubly Linked List Implementation
class QueList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, que : int):
        temp = Node(que)
        temp.next = self.head
        if(self.head):
            self.head.prev = temp
        self.head = temp
    
    def delete(self, key : int):
        temp = self.head

        if temp and temp.que == key:
            self.head = temp.next
            temp = None
            return
        
        while(temp.next):
            temp = temp.next

            if temp.que == key:
                temp.prev.next = temp.next
                if(temp.next):
                    temp.next.prev = temp.prev
                temp = None
                return
            
        print(key,"doesn't exisit")