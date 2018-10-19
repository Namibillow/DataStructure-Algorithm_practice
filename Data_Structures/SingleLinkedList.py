class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # InsertAtEnd — Inserts given element at the end of the linked list
    def insert_end(self, newNode):
        if self.head is None:
            self.head = newNode
        else:
            lastNode = self.head
            while True:
                if lastNode.next is None:
                    break
                lastNode = lastNode.next
            lastNode.next = newNode

    # InsertAtHead — Inserts given element at the start/head of the linked list
    def insert_head(self, newNode):
        if self.head is None:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode

    def insert_by_index(self, index, newNode):
        if index == 0:  # if index is 0 then change head
            newNode.next = self.head
            self.head = newNode
        else:
            currNode = self.head
            prevNode = None
            i = 0
            while currNode is not None:
                if i == index:
                    prevNode.next = newNode
                    newNode.next = currNode
                    return

                i += 1
                prevNode = currNode
                currNode = currNode.next

            return "Error no index found"
        return

    def printList(self):
        if self.head is None:
            print("list is empty")
            return
        currNode = self.head
        while True:
            if currNode is None:
                break
            print(currNode.data)
            currNode = currNode.next

    # Search — Returns the given element from a linked list
    def search(self, x):
        currNode = self.head
        while currNode != None:
            if currNode.data == x:
                return True
            currNode = currNode.next
        return False

    # Delete — Deletes given index from the linked list
    def delete_index(self, index):
        currNode = self.head
        prevNode = None

        i = 0
        while currNode != None:
            if (i == index):
                if prevNode:
                    prevNode.next = currNode.next

                else:  # if deleting the head
                    self.head = currNode.next
                return True

            prevNode = currNode
            currNode = currNode.next
            i += 1

        return False

    # Delete — Deletes given element from the linked list
    def delete_value(self, value):
        currNode = self.head
        prevNode = None

        while currNode != None:
            if (value == currNode.data):
                if prevNode:
                    prevNode.next = currNode.next

                else:
                    self.head = currNode.next
                return True

            prevNode = currNode
            currNode = currNode.next

        return False

    # DeleteAtHead — Deletes first element of the linked list
    def delete_at_head(self):
        if self.head:
            self.head = self.head.next

    # DeleteAtTail — Deletes last element of the linked list
    def delete_at_tail(self):
        currNode = self.head
        prevNode = None

        if self.head == None:
            return "can't delete empty list duh"

        if self.head.next == None:
            self.head = None

        else:
            while currNode.next:
                prevNode = currNode
                currNode = currNode.next

            prevNode.next = None

        return True

    # isEmpty — Returns true if the linked list is empty
    def isEmpty(self):
        if self.head is None:
            print("Yes it is Empty")
            return True

        print("no it's not empty")
        return False

    def size(self):
        currNode = self.head
        i = 0
        while currNode:
            i += 1
            currNode = currNode.next
        return i

    # Reverse a linked list
    def reverseList(self):
        if self.head == None:
            return

        prevNode = None
        currNode = self.head
        nextNode = currNode.next

        while currNode:
            currNode.next = prevNode
            prevNode = currNode
            currNode = nextNode

            if nextNode:
                nextNode = nextNode.next

        self.head = prevNode

    def reverseRecurse(self):
        self.reverseRecurseHelper(self.head)

    def reverseRecurseHelper(self, node):
        if node.next == None:
            self.head = node
            return

        self.reverseRecurseHelper(node.next)
        temp = node.next
        temp.next = node
        node.next = None

    def findMiddle(self):
        fast_node, slow_node = self.head, self.head

        if self.head:
            while fast_node is not None and fast_node.next is not None:
                fast_node = fast_node.next.next
                slow_node = slow_node.next

            return slow_node.data

        return "Nothing in the list"


# Some testing
print("Example1:")
SLL = LinkedList()
SLL.insert_head(Node(4))
SLL.insert_head(Node(5))
SLL.insert_head(Node(6))
SLL.insert_head(Node(7))
SLL.insert_head(Node(8))
SLL.insert_end(Node(1))
SLL.insert_end(Node(2))
SLL.insert_end(Node(3))

print("---Is empty---")
SLL.isEmpty()

print("---Searching for 4--")
print(SLL.search(4))  # Return true
print("---Searching for 11--")
print(SLL.search(11))  # Return false

print("--print list--")
SLL.printList()

print("--deleting nodes by index--")
print(SLL.delete_index(0))
print(SLL.delete_index(0))
print(SLL.delete_index(1))

print("--deleting nodes by value--")
print(SLL.delete_value(4))
print(SLL.delete_value(4))  # Check if it is really deleted
print(SLL.delete_value(1))

print("--print list--")
SLL.printList()


print("Example2:")
# Check for empt list
test = LinkedList()
print("---Deleting index at 0--")
print(test.delete_index(0))

print("---Searching for 5--")
print(test.search(5))

print("---Is empty---")
print(test.isEmpty())


test.insert_end(Node(1))
test.insert_end(Node(2))
test.insert_end(Node(3))
test.insert_end(Node(4))
test.insert_end(Node(5))
test.insert_end(Node(6))
test.insert_end(Node(7))
test.insert_end(Node(8))
test.insert_end(Node(9))
test.insert_end(Node(10))
# print(test.delete_at_tail())
# print(test.delete_at_tail())
# print(test.delete_at_tail())
# print(test.delete_at_tail())
# print(test.delete_at_tail())

print("---print list---")
test.printList()

print("---testing insert at certain position")
test.insert_by_index(1, Node(100))
test.insert_by_index(1, Node(200))

print("---print list---")
test.printList()

print("--reverse list--")
# test.reverseList()
test.reverseRecurse()

print("---print list---")
test.printList()

print("---Checking---")
print(test.size())

print("---checking the middle number--")
print(test.findMiddle())

# Test 3:
emptylist = LinkedList()
print("---print list---")
emptylist.printList()

print("--reverse list--")
emptylist.reverseList()

print("---print list---")
emptylist.printList()

emptylist.insert_by_index(0, Node(4))
emptylist.insert_by_index(0, Node(5))

print("---print list---")
emptylist.printList()

# Detect loop in a linked list
# Return Nth node from the end in a linked list
# Remove duplicates from a linked list
