import typing


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


def remove(a: Node):
    checked = []
    while a.next != None:
        b = a.next
        if a.value not in checked:
            while b.next != None:
                if a.value == b.value:
                    b.prev.next = b.next
                    print("YO")
                    print(a, b)
                b = b.next
            checked.append(a)
        a = a.next
    return a


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
remove(a)
check = a
print(check.value)
while check.next != None:
    print(check.next.value)
    check = check.next
