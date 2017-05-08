class Node:

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


def remove_node(location):
    location.data = location.next.data
    location.next = location.next.next


def print_linked_list(head):
    node = head
    values = ""
    values = values + " " + str(node.data)
    while(node.next is not None):
        node = node.next
        values = values + " " + str(node.data)
    print("linked list values : ", values)


if __name__ == "__main__":
    third = Node(3)
    second = Node(2, third)
    head = Node(1, second)
    print_linked_list(head)
    remove_node(second)
    print_linked_list(head)
