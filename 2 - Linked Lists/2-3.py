import typing


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


def del_middle(a):
    while a.next != None:
        a.value = a.next.value
        a = a.next


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
del_middle(b_1)
check = a
while check.value != None:
    print(check.value)
    check = check.next
