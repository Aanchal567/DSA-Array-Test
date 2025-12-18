class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Creating nodes
a = Node(5)
b = Node(3)
c = Node(7)

# Linking nodes
a.next = b
b.next = c

# Head of linked list
head = a

# Function to print linked list
def printLinkedlist(head):
    curr = head
    while curr != None:
        print(curr.data, end=" -> ")  # show link
        curr = curr.next              # move to next node
    print("None")                     # end of list

# Call the function
printLinkedlist(head)
