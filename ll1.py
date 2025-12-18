class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class SinglyLinkedList:
    def __init__(self) -> None:
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
    
    def traverse(self):
        if not self.head:
            print("Singly linked list is empty")
        else:
            current = self.head
            while current is not None:
                print(current.val, end=" ")
                current = current.next
            print()
    
    def insert_at(self, val, position):
        new_node = Node(val)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            count = 0
            # Traverse to the node just before the position
            while current is not None and count < position - 1:
                current = current.next
                count += 1
            
            if current is None:
                print("Position out of bounds")
                return
            
            # Insert new_node
            new_node.next = current.next
            current.next = new_node

# Testing
sll = SinglyLinkedList()
sll.append(5)
sll.append(10)
sll.append(7)
sll.append(8)  

sll.traverse()  # Output: 5 10 7 8

sll.insert_at(15, 2)  # Insert 15 at position 2
sll.traverse()  # Output: 5 10 15 7 8

sll.insert_at(20, 0)  # Insert 20 at head
sll.traverse()  # Output: 20 5 10 15 7 8
