from src.linkedlist import LinkListException, Node, print_linked_list, linked_list_from_array


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
