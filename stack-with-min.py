class Node:

    def __init__(self, value, current_min):
        self.value = value
        self.current_min = current_min


class Stack:

    def __init__(self):
        self.values = []

    def push(self, value):
        current_min = self.peek_min()
        if(current_min):
            new_min = min(current_min, value)
        else:
            new_min = value
        push_node = Node(value, new_min)
        self.values.append(push_node)

    def pop(self):
        if(self.values):
            pop_value = self.values[-1].value
            self.values = self.values[:-1]
        else:
            pop_values = None
        return pop_value

    def peek_min(self):
        if(self.values):
            min_value = self.values[-1].current_min
        else:
            min_value = None
        return min_value


if __name__ == "__main__":
    stack = Stack()
    values = [1, 2, 6, 3, 2, -4, 5]
    for value in values:
        stack.push(value)

    print(stack.peek_min())
    import pdb
    pdb.set_trace()
