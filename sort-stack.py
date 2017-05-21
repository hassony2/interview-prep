from src.stack import Stack


def sort_stack(stack):
    buffer_stack = Stack()
    while(not stack.is_empty()):
        value = stack.pop()
        if(buffer_stack.is_empty):
            buffer_stack.push(value)
        else:
            if(not buffer_stack.is_empty()):
                while(buffer_stack.peek() > value):
                        temp = buffer_stack.pop()
                        stack.push(temp)
            else:
                buffer_stack.push(value)
    return buffer_stack


if __name__ == "__main__":
    stack = Stack()
    values = [2, 7, 3, 5, 8, 2, 10, 4, 5, 11, 1]
    for value in values:
        stack.push(value)
    print(stack.items)
    sorted_stack = sort_stack(stack)
    print(sorted_stack.items)
