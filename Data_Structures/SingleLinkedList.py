class Node:
    def __init__(self, data=0):
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
            if num >= k:
                break

        curr = head
        if num < k:
            return curr

        while(curr is not None and count < k):
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
            count += 1

        if next is not None:
            head.next = self.reverse_k_nodes(k, next)

        return prev

    # Same as previous but different implementation
    def reverseKGroup(self, head, k):
        dummy = Node()
        dummy.next = head
        pre = dummy
        while head:
            cur = head
            cnt = 0
            while cur and cnt != k:
                cur = cur.next
                cnt += 1
            if cnt != k:
                break
            then = head.next
            for i in range(k - 1):
                head.next = then.next
                then.next = pre.next
                pre.next = then
                then = head.next
            pre = head
            head = head.next
        return dummy.next

    # given non negative integer m, if each k number in List occurs more than m times than delete
    def remove_n_occurence(self, m):

        dummy = Node()
        dummy.next = self.head

        prev = dummy
        curr = self.head

        if m == 1:
            self.head = None
            return

        while curr is not None:
            count = 1
            while curr.next is not None and prev.next.data == curr.next.data:
                print("this is ", curr.next.data)
                count += 1
                curr = curr.next

            print("count", count)
            if prev.next is curr:
                print("current ain't walking")
                prev = prev.next

            elif count >= m:
                print("removind!")
                prev.next = curr.next
                # print(curr.next.data)

            else:  # if nothing got deleted than
                prev = curr

            curr = curr.next
        return dummy.next

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
    List1, List2 = List1.head, List2.head
    while List1 and List2:
        if List1.data < List2.data:
            tail.next, List1 = List1, List1.next
        else:
            tail.next, List2 = List2, List2.next

        tail = tail.next

    tail.next = List1 or List2
    return new_head.next

# Takes O(n) because of counting total nodes


def shift_by_k(L, k):
    if not L:
        return L

    tail, n = L.head, 1

    # Count total nodes and make tail points to original tail
    while tail.next:
        tail = tail.next
        n += 1

    # mod n by k since there is possibility of k > n
    k %= n
    if k == 0:
        return L

        # Make it cyclic by pointing tail.next to list's original head
    tail.next = L.head
    steps_to_new_head, new_tail = n - k, tail
    while steps_to_new_head:
        steps_to_new_head -= 1
        new_tail = new_tail.next

    new_head = new_tail.next
    new_tail.next = None
    return new_head

# Even-odd merge starting index as 0 as even
# L is pointing at the head of List L


def even_odd_merge(L):
    L = L.head
    if not L:
        return L

    even_dummy_head, odd_dummy_head = Node(), Node()
    tails, turn = [even_dummy_head, odd_dummy_head], 0

    while L:
        tails[turn].next = L
        L = L.next
        tails[turn] = tails[turn].next
        turn ^= 1

    tails[1].next = None
    tails[0].next = odd_dummy_head.next
    return even_dummy_head.next

# Hint: find middle node of the list
# reverse the second half
# check if it's equal
# Empty or only 1 node list returns true


def is_palindrom(L):
    slow = fast = L.head
    while fast and fast.next:
        fast, slow = fast.next.next, slow.next

    second_half_iter = LinkedList()
    second_half_iter.insert_end(slow)
    second_half_iter.reverseList()

    first_half_iter, second_half_iter = L.head, second_half_iter.head
    while second_half_iter and first_half_iter:
        if second_half_iter.data != first_half_iter.data:
            return False
        second_half_iter, first_half_iter = second_half_iter.next, first_half_iter.next

    return True

# Given List and some number x (assume x is in the list), change the order of the list where nodes that are less than x is appended front of the x and vice versa


def list_pivoting(L, x):
    '''
    Idea is splitting the list into three and combine them back
    '''
    L = L.head
    less_head = less_iter = Node()
    equal_head = equal_iter = Node()
    greater_head = greater_iter = Node()

    while L:
        if L.data < x:
            less_iter.next = L
            less_iter = less_iter.next
        elif L.data == x:
            equal_iter.next = L
            equal_iter = equal_iter.next
        else:
            greater_iter.next = L
            greater_iter = greater_iter.next
        L = L.next

    greater_iter.next = None
    equal_iter.next = greater_head.next
    less_iter.next = equal_head.next
    return less_head.next

# Given two lists where MOST significant digit come first, add them
# EX: L1=1->3->4, L2=2->2
# then L3 = 134+ 22 = 156 => 1->5->6
# assume each number in the node is 0-9 (one digit)
# takes O(n+m) time complexity with O(max(n,m)) space where n and m is the size of the lists
def add_two_numbers(L1, L2):
    L1_size, L2_size = 0, 0
    # If one of the list is empty then return other
    if L1 is None:
        return L2
    if L2 is None:
        return L1

    L1_head = L1.head
    L2_head = L2.head

    # count the size of the each list
    while L1_head:
        L1_size += 1
        L1_head = L1_head.next

    while L2_head:
        L2_size += 1
        L2_head = L2_head.next

    # make the size equal
    if L1_size > L2_size:
        diff = L1_size - L2_size
        while diff:
            zero = Node()
            zero.next = L2.head
            L2.head = zero
            diff -= 1

    elif L2_size > L1_size:
        diff = L2_size - L1_size
        while diff:
            zero = Node()
            zero.next = L1.head
            L1.head = zero
            diff -= 1

    result, carry = add_two_numbers_helper(L1.head, L2.head, 0)
    if carry == 1:
        # print("Carry is ", carry)
        add_one = Node(1)
        add_one.next = result
        return add_one
    return result


def add_two_numbers_helper(L1_head, L2_head, carry):
    '''
    Recursively do the sum from least significant digit and return the list and carry
    '''
    if L1_head is None:
        return None, 0
    total = 0

    dummy = Node()
    dummy.next, prev_carry = add_two_numbers_helper(L1_head.next, L2_head.next, carry)

    total = L1_head.data + L2_head.data + prev_carry
    carry = total // 10
    total = total % 10

    dummy.data = total

    return dummy, carry

SLL = LinkedList()
SLL.insert_end(Node(0))
# SLL.insert_end(Node(9))
# SLL.insert_end(Node(9))

test = LinkedList()
test.insert_end(Node(2))
# test.insert_end(Node(1))
# test.insert_end(Node(3))

dum = LinkedList()
sum_result = add_two_numbers(test,SLL)
dum.insert_end(sum_result)
dum.printList()

# Testing Palindrom
# Pal = LinkedList()
# Pal.insert_end(Node(1))
# Pal.insert_end(Node(1))
# Pal.insert_end(Node(3))
# Pal.insert_end(Node(3))
# Pal.insert_end(Node(2))
# Pal.insert_end(Node(1))
# print(is_palindrom(Pal))

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


# test = LinkedList()
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

# # test.head = test.reverseKGroup(test.head, 3)
# # test.head = test.reverse_k_nodes(3, test.head)
# test.printList()

# print("here")
# test2 = LinkedList()
# test2.insert_end(Node(2))
# test2.insert_end(Node(200))

# test3 = LinkedList()
# test3.head = merge_lists_two(test, test2)


# test3.printList()
# print("here")
# test4 = LinkedList()
# test4.insert_end(Node(1))
# test4.insert_end(Node(1))
# test4.insert_end(Node(1))
# test4.insert_end(Node(2))
# test4.insert_end(Node(2))
# test4.insert_end(Node(2))
# test4.insert_end(Node(2))
# test4.insert_end(Node(3))
# test4.insert_end(Node(3))
# test4.insert_end(Node(3))
# test4.insert_end(Node(3))
# test4.insert_end(Node(3))
# test4.insert_end(Node(3))
# test4.insert_end(Node(3))
# test4.insert_end(Node(10))
# test4.insert_end(Node(10))
# test4.insert_end(Node(10))

# print("Testing")
# h = test4.remove_n_occurence(3)
# print("printing")
# while h:
#     print(h.data)
#     h = h.next
# test4.printList() can't be called if all item was removed


# test5 = LinkedList()
# test5.insert_end(Node(0))
# test5.insert_end(Node(1))
# test5.insert_end(Node(2))
# test5.insert_end(Node(3))
# new_list = LinkedList()
# print("testing shift")
# new_list.insert_end(shift_by_k(test5, 2))
# new_list.printList()

#Comment out shift_by_k
# print("testing odd_even")
# nl = LinkedList()
# nl.insert_end(even_odd_merge(test5))
# nl.printList()
