from src.stack import Stack


def add_tower(tower_height, stack_1):
    for height in range(tower_height):
        stack_1.push(tower_height - height)


def print_towers(stack_1, stack_2, stack_3):
        print("towers")
        print(stack_1.items)
        print(stack_2.items)
        print(stack_3.items)


def move_tower(n, origin=stack_1, destination=stack_2,
               intermediate=stack_3, display_progress=True):
    """
    moves the tower from stack_1 to stack_2
    (by using stack_3)
    """
    if(n == 1):
        if(stack_1.length()):
            value = stack_1.pop()
            stack_2.push(value)
            print_towers(tower_1, tower_2, tower_3)
    if(n >= 2):
        move_tower(n-1, stack_1, stack_3, stack_2)
        move_tower(1, stack_1, stack_2, stack_3)
        move_tower(n-1, stack_3, stack_2, stack_1)


if __name__ == "__main__":
    tower_1 = Stack()
    tower_2 = Stack()
    tower_3 = Stack()
    add_tower(5, tower_1)
    move_tower(5, tower_1, tower_2, tower_3)
    print_towers(tower_1, tower_2, tower_3)
