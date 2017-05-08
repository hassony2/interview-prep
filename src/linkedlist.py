class LinkListException(Exception):
    pass


class Node:

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


def linked_list_from_array(array_values):
    if(array_values):
        head = Node(array_values[0])
        next_node = head
        for value in array_values[1:]:
            new_node = Node(value)
            next_node.next = new_node
            next_node = new_node
    else:
        head = None
    return head


def print_linked_list(head):
    node = head
    values = ""
    values = values + " " + str(node.data)
    while(node.next is not None):
        node = node.next
        values = values + " " + str(node.data)
    print("linked list values : ", values)


def print_online(head):
    node = head
    print("linked list values :")
    print(node.data)
    while(node.next is not None):
        node = node.next
        print(node.data)
