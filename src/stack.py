class Stack:

    def __init__(self):
        self.items = []

    def pop(self):
        if(self.items):
            pop_value = self.items[-1]
            self.items = self.items[:-1]
        else:
            pop_value = None
        return pop_value

    def push(self, value):
        self.items.append(value)

    def length(self):
        return len(self.items)
