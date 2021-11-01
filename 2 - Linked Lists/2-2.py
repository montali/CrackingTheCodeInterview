from collections import deque


class Node:
    def __init__(self, value):
        self.value = value
        if value != None:
            self.next = Node(None)
        else:
            self.next = None
        self.prev = None

    def __repr__(self) -> str:
        return str(self.value)


def k_to_last(a, k):
    elems = deque()
    while a.value != None:
        if len(elems) >= k:
            elems.popleft()
        elems.append(a)
        a = a.next
    return elems


a = Node(5)
b = Node(6)
b_1 = Node(6)
c = Node(7)
a.next = b
b.next = b_1
b_1.next = c
b_1.prev = b
b.prev = a
c.prev = b_1
print(k_to_last(a, 2))
