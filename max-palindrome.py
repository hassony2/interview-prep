# your task is to complete this function
# function should return an integer


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def max_palindrome(head):
    """
    Computes size of max palindrome of linked list that starts at head
    Example:
    0->1->2->3->2->7 => 3
    """
    max_size = 0
    # if linked list not empty minimum palindrome size is 1
    if(head):
        max_size = 1
    reversed = Node(head.data)
    if(head.next):
        next_node = head.next
        pair_max = max_centered(next_node, reversed)
        max_size = max(pair_max, max_size)
        while next_node.next is not None:
            current_value = next_node.data
            next_node = next_node.next
            impair_max = max_centered(next_node, reversed, True)

            # Add node to reversed linked list
            next_reversed = Node(current_value, reversed)
            reversed = next_reversed

            pair_max = max_centered(next_node, reversed)
            max_size = max(max_size, pair_max, impair_max)
    return max_size


def max_centered(forward, reversed, center=False):
    """
    Returns the size of the palindrome that has forward as right part
    reversed as left part and optionnally center as middle value
    Checks to what extent forward and reversed are mirrors of each other

    :param forward: Node that is the beginning of the right linked list
    :param backward: Node that is the beginning of the reversed left linked list
    :param center: boolean indicating if central value exists
    """
    pal_length = 0
    if center:
        pal_length = 1
    if(forward.data == reversed.data):
        print(forward.data, reversed.data)
        pal_length += 2
        while(forward.next and reversed.next):
            forward = forward.next
            reversed = reversed.next
            if (forward.data == reversed.data):
                print('hey')
                pal_length += 2
            else:
                break
    return pal_length


# linked list utilities
def print_linked_list(head):
    """
    Prints linked elements
    """ 
    while head.next:
        head = head.next
        print(head.data)


def linked_list_from_array(array):
    if(array):
        head = Node(array[0])
        current_node = head
    for value in values[1:]:
        next_ = Node(value)
        current_node.next = next_
        current_node = current_node.next
    return head

if __name__ == "__main__":
    values = [0, 1, 2, 3, 4, 3, 2, 1, 2, 7]
    print('expected palindrom size for', values, ': 7')
    head = linked_list_from_array(values)
    print('computed max palindrom size : ', max_palindrome(head))

    values = [1, 2, 2, 1, 1, 2, 3]
    print('expected palindrom size for', values, ': 4')
    head = linked_list_from_array(values)
    print('computed max palindrom size : ', max_palindrome(head))

    values = [59, 96, 30, 38, 36, 94, 19, 29, 44, 12, 29, 30, 77, 5, 44, 64, 14, 39, 7, 41, 5, 19]
    head = linked_list_from_array(values)
    print(max_palindrome(head))
