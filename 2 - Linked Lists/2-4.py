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


def partition(a, p):
    end = a
    while end.next.value != None:
        end = end.next
    i = end.next
    i.prev = end
    while a.next != end:
        next_check = a.next
        if a.value >= p:
            a.prev.next = a.next
            a.prev = i.prev
            a.next = Node(None)
            i = a
            i.prev.next = i
        a = next_check


a = Node(4)
b = Node(10)
b_1 = Node(6)
c = Node(7)
a.next = b
b.next = b_1
b_1.next = c
b_1.prev = b
b.prev = a
c.prev = b_1
partition(a, 6)
check = a
while check.value != None:
    print(check.value)
    check = check.next
