class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


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


DLL = LinkedList()
DLL.push_front(Node(5))
DLL.push_front(Node(4))
DLL.push_front(Node(3))
DLL.push_front(Node(2))
DLL.push_back(Node(6))
DLL.push_back(Node(7))
DLL.push_back(Node(8))

DLL.displaly()
