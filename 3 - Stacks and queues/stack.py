class EmptyStackException(Exception):
    pass


class StackNode:
    def __init__(self, data):
        self.next = None
        self.data = data

    def __repr__(self) -> str:
        return f"Node, data={self.data}"


class Stack:
    def __init__(self):
        self.top = None

    def pop(self):
        if self.top == None:
            raise EmptyStackException
        item = self.top
        self.top = self.top.next
        return item

    def add(self, data):
        node = StackNode(data)
        node.next = self.top
        self.top = node

    def peek(self):
        if self.top == None:
            raise EmptyStackException
        return self.top.data

    def __repr__(self):
        next_node = self.top
        while next_node != None:
            print(next_node)
            next_node = next_node.next

if __name__ == "__main__":
    st = Stack()
    st.add(5)
    st.add(6)
    st.add(7)
    while True:
        print(st.pop())
