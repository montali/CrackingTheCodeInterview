class EmptyQueueException(Exception):
    pass

class QueueNode:
    def __init__(self, data):
        self.next = None
        self.data = data

    def __repr__(self) -> str:
        return f"Node, data={self.data}"

class Queue:
    def __iter__(self):
        return self
    def __init__(self):
        self.first = None
        self.last = None
    def add(self, data):
        if self.first == self.last == None:
            self.first = QueueNode(data)
            self.last = self.first
        else:
            node = QueueNode(data)
            self.last.next = node
            self.last = node
    def __next__(self):
        if self.first == None:
            raise StopIteration
        else:
            item = self.first
            self.first = item.next
            return item.data
    def peek(self):
        if self.first == None:
            raise EmptyQueueException
        else:
            return self.first.data
    def __repr__(self):
        next_node = self.first
        while next_node != None:
            print(next_node)
            next_node = next_node.next


que = Queue()
que.add(5)
que.add(6)
que.add(7)
for element in que:
    print(element)

