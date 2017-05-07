class LinkListException(Exception):
    pass


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


def linked_list_from_array(array_values):
    head = Node(array_values[0])
    next_node = head
    for value in array_values[1:]:
        new_node = Node(value)
        next_node.next = new_node
        next_node = new_node
    return head


def print_linked_list(head):
    node = head
    values = ""
    values = values + " " + str(node.data)
    while(node.next is not None):
        node = node.next
        values = values + " " + str(node.data)
    print("linked list values : ", values)


def find_nth_to_last(head, n):
    """
    Returns data associated to the node that is at
    the n-th before last position

    Example:
    list: 1->2->-3->2->1 if n=2 ==> 2nd to last: 3
    """
    first_pointer = head
    second_pointer = head
    for i in range(n):
        if(first_pointer.next):
            first_pointer = first_pointer.next
        else:
            raise LinkListException("Linked list too short")
    while(first_pointer.next):
        first_pointer = first_pointer.next
        second_pointer = second_pointer.next
    return second_pointer.data


if __name__ == "__main__":
    link_values = [1, 2, 3, 4, 2, 3]
    link_list = linked_list_from_array(link_values)
    print_linked_list(link_list)
    n = 2
    nth_to_last = find_nth_to_last(link_list, n)
    print(n, 'th element to last : ', nth_to_last)
