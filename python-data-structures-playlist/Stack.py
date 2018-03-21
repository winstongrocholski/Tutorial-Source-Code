class Stack:

    def __init__(self):
        self.items = [] # python list

    def __len__(self):
        return len(self.items)

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        else:
            return self.items.pop()

    def peak(self):
        if self.is_empty():
            return "Stack is empty"
        else:
            return self.items[-1]
