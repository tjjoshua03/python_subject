class Stack:
    def __init__(self):
        self.list = []

    def push(self, node):
        if node in self.list:
            raise ValueError(f"{node} already exists")
        self.list.append(node)
        return True

    def pop(self):
        if not self.is_empty():  
            popped_value = self.list.pop()
            return popped_value
        else:
            raise IndexError("Pop from an empty stack")

    def is_empty(self):
        if len(self.list) == 0:
            return True
        else:
            return False

    def peek(self):
        return self.list

#Test Code

s = Stack()
print(s.push(3))
print(s.push(4))
print(s.push(5))
print(s.peek())
print(s.pop())
print(s.is_empty())
print(s.push(3))