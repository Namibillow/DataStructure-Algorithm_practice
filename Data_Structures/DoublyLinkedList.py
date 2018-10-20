class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def push_back(self, newNode):
        if self.head is None:
            self.head = newNode
            self.tail = self.head
        else:
            self.tail.next = newNode
            self.tail = newNode

    def push_front(self, newNode):
        if self.head is None:
            self.head = newNode
            self.tail = self.head
        else:
            newNode.next = self.head
            self.head = newNode

    def displaly(self):
        if self.head is None:
            print("its empty")
            return
        else:
            currNode = self.head
            while currNode:
                print(currNode.data)
                currNode = currNode.next


def merge_list(List1, List2):
    new_head = tail = LinkedList()

    while List1 and List2:
        if List1.data < List2.data:
            tail.next, List1.prev, List1 = List1, tail, List1.next

        else:
            tail.next, List2.prev, List2 = List2, tail, List2.next

        tail = tail.next

    if List1:
        tail.next = List1
        List1.prev = tail
    else:
        tail.next = List2
        List2.prev = tail

    return new_head.next


# Testing #
DLL = LinkedList()
DLL.push_front(Node(5))
DLL.push_front(Node(4))
DLL.push_front(Node(3))
DLL.push_front(Node(2))
DLL.push_back(Node(10))

DLL2 = LinkedList()
DLL2.push_back(Node(1))
DLL2.push_back(Node(6))
DLL2.push_back(Node(7))
DLL2.push_back(Node(8))

print("list 1")
DLL.displaly()

print("List 2")
DLL2.displaly()

print("ok")

new_list = (merge_list(DLL.head, DLL2.head))
while new_list:
    print(new_list.data)
    new_list = new_list.next
