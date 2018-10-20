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

    # InsertByIndex = Inserts given element at the specified index
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

    # Prints the list item from head to tail
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

    # returns the size of the list
    def size(self):
        currNode = self.head
        i = 0
        while currNode:
            i += 1
            currNode = currNode.next
        return i

    # Reverse a linked list in iterative way
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

    # Reverse a linked list in recursive way
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

    # Finds the middle element of the linked list
    def findMiddle(self):
        fast_node, slow_node = self.head, self.head

        if self.head:
            while fast_node is not None and fast_node.next is not None:
                fast_node = fast_node.next.next
                slow_node = slow_node.next

            return slow_node.data

        return "Nothing in the list"

    # Determine whether there is loop in the list (list revisiting already traversed node)
    def detect_loop(self):
        s = set()
        currNode = self.head
        while currNode:
            if currNode in s:
                return True

            s.add(currNode)
            print(s)
            currNode = currNode.next

        return False

    # n’th node from the end of a Linked List where at last index starts as 1
    def nth_from_end(self, index):
        i = self.size()
        currNode = self.head
        while currNode and i is not 0:
            if (index == i):
                print(currNode.data)
                return
            i -= 1
            currNode = currNode.next

        print("Out of range")
        return

    # Remove the duplicated data takes O(n^2)
    def remove_dups(self):
        outerNode, innerNode = self.head, None

        while(outerNode is not None and outerNode.next is not None):
            innerNode = outerNode
            while(innerNode.next is not None):
                if outerNode.data == innerNode.next.data:
                    innerNode.next = innerNode.next.next
                else:
                    innerNode = innerNode.next

            outerNode = outerNode.next

    # Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.
    def reverse_k_nodes(self, k, head):
        curr = head
        next = None
        prev = None

        count = 0
        num = 0
        while curr:
            num += 1
            curr = curr.next

        curr = head
        while(curr is not None and count < k):
            if num < k:
                return curr

            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
            count += 1

        if next is not None:
            head.next = self.reverse_k_nodes(k, next)

        return prev


# merge two sorted list into a one list


def merge_lists(list1, list2, merged_list):
    curr1 = list1.head
    curr2 = list2.head
    # O(n)
    while True:
        if curr1 is None:
            merge_lists.insert_end(curr2)
            return

        if curr2 is None:
            merge_lists.insert_end(curr1)
            return

        if curr1.data < curr2.data:
            curr1Next = curr1.next
            curr1.next = None
            merged_list.insert_end(curr1)
            curr1 = curr1Next
        else:
            curr2Next = curr2.next
            curr2.next = None
            merge_lists.insert_end(curr2)
            curr2 = curr2Next


# cleaner merge list
def merge_lists_two(List1, List2):
    new_head = tail = LinkedList()

    while List1 and List2:
        if List1.data < List2.data:
            tail.next, List1 = List1, List1.next
        else:
            tail.next, List2 = List2, List2.next

        tail = tail.next

    tail.next = List1 or List2
    return new_head.next

    # Test 1
# print("Example1:")
# SLL = LinkedList()
# SLL.insert_head(Node(4))
# SLL.insert_head(Node(5))
# SLL.insert_head(Node(6))
# SLL.insert_head(Node(7))
# SLL.insert_head(Node(7))
# SLL.insert_head(Node(7))
# SLL.insert_head(Node(8))
# SLL.insert_end(Node(1))
# SLL.insert_end(Node(2))
# SLL.insert_end(Node(3))

# print("---Is empty---")
# SLL.isEmpty()

# print("--nth node from end--")
# SLL.nth_from_end(3)  # should display 1
# SLL.nth_from_end(1)  # should be 3

# print("--print list--")
# SLL.printList()

# print("--removing duplicated stuff--")
# SLL.remove_dups()

# print("---Searching for 4--")
# print(SLL.search(4))  # Return true
# print("---Searching for 11--")
# print(SLL.search(11))  # Return false

# print("--print list--")
# SLL.printList()

# print("--deleting nodes by index--")
# print(SLL.delete_index(0))
# print(SLL.delete_index(0))
# print(SLL.delete_index(1))

# print("--deleting nodes by value--")
# print(SLL.delete_value(4))
# print(SLL.delete_value(4))  # Check if it is really deleted
# print(SLL.delete_value(1))

# print("--print list--")
# SLL.printList()

# # Test 2
# print("Example2:")
# # Check for empt list
# test = LinkedList()
# print("---Deleting index at 0--")
# print(test.delete_index(0))

# print("---Searching for 5--")
# print(test.search(5))

# print("---Is empty---")
# print(test.isEmpty())

# test.insert_end(Node(1))
# test.insert_end(Node(2))
# test.insert_end(Node(3))
# test.insert_end(Node(4))
# test.insert_end(Node(5))
# test.insert_end(Node(6))
# test.insert_end(Node(7))
# test.insert_end(Node(8))
# test.insert_end(Node(9))
# test.insert_end(Node(10))
# test.insert_end(Node(11))
# # print(test.delete_at_tail())
# # print(test.delete_at_tail())
# # print(test.delete_at_tail())
# # print(test.delete_at_tail())
# # print(test.delete_at_tail())

# print("---print list---")
# test.printList()

# print("---testing insert at certain position")
# test.insert_by_index(1, Node(100))
# test.insert_by_index(1, Node(200))

# print("---print list---")
# test.printList()

# print("--reverse list--")
# # test.reverseList()
# test.reverseRecurse()

# print("---print list---")
# test.printList()

# print("---Checking---")
# print(test.size())

# print("---checking the middle number--")
# print(test.findMiddle())

# # Test 3:
# print("Example3:")
# emptylist = LinkedList()

# print("---print list---")
# emptylist.printList()

# print("--reverse list--")
# emptylist.reverseList()

# print("---print list---")
# emptylist.printList()

# emptylist.insert_by_index(0, Node(4))
# emptylist.insert_by_index(0, Node(5))

# print("---print list---")
# emptylist.printList()

# print("--nth node from end--")
# emptylist.nth_from_end(3)
# # Detect loop in a linked list
# # Return Nth node from the end in a linked list
# # Remove duplicates from a linked list

# # test 4
# print("Example4:")
# a = LinkedList()
# a.insert_end(Node(4))
# a.insert_end(Node(5))
# a.insert_end(Node(6))
# print("---print list---")
# a.printList()
# # make it loop: 6 points to 5
# a.head.next.next.next = a.head.next
# print("there is a loop:", a.detect_loop())


test = LinkedList()
test.insert_end(Node(1))
test.insert_end(Node(2))
test.insert_end(Node(3))
# test.insert_end(Node(4))
# test.insert_end(Node(5))
# test.insert_end(Node(6))

test.head = test.reverse_k_nodes(5, test.head)
test.printList()
