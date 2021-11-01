from stack import Stack, StackNode, EmptyStackException

class StackFullException(Exception):
    pass
class StackForSets(Stack):
    def __init__(self,max_capacity, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.capacity = 0
        self.max_capacity = max_capacity
        self.next_stack = None
    def pop(self):
        returnable = super().pop()
        # If we're here, the stack ain't empty
        self.capacity -= 1
        return returnable
    def add(self, *args):
        if self.capacity == self.max_capacity:
            raise StackFullException
        super().add(*args)
        self.capacity += 1
    def __len__(self):
        return self.capacity

class StackSet():
    def __init__(self, capacity):
        self.top_stack = None
        self.capacity = capacity
    def pop(self):
        if self.top_stack == None:
            raise EmptyStackException
        item = None
        while item == None:
            try:
                item = self.top_stack.pop()
            except EmptyStackException:
                self.top_stack = self.top_stack.next_stack
                if self.top_stack == None:
                    raise EmptyStackException
        return item.data
    def add(self, data):
        node = StackNode(data)
        if self.top_stack == None:
            self.top_stack = StackForSets(self.capacity)
        while True:
            try:
                self.top_stack.add(node)
                break
            except StackFullException:
                new_stack = StackForSets(self.capacity)
                new_stack.next_stack = self.top_stack
                self.top_stack = new_stack
    

st = StackSet(2)
st.add(5)
st.add(6)
st.add(7)
st.add(8)
while True:
    print(st.pop())
