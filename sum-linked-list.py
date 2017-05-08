# Node utilities


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


# Exercise specific code

def sum_linked(digits_1, digits_2):
    if(digits_1.data is not None and digits_2.data is not None):
        digit_sum = digits_1.data + digits_2.data
        retenue = digit_sum // 10
        node_digit = digit_sum % 10
        head = Node(node_digit)
        current = head
    while(digits_1.next is not None or digits_2.next is not None):
        digit_sum = retenue
        if(digits_1.next is not None):
            digits_1 = digits_1.next
            digit_sum += digits_1.data
        if(digits_2.next is not None):
            digits_2 = digits_2.next
            digit_sum += digits_2.data

        retenue = digit_sum // 10
        node_digit = digit_sum % 10
        new_node = Node(node_digit)
        current.next = new_node
        current = current.next

    return head


if __name__ == "__main__":
    digit_1_values = [1, 2, 3, 4, 2, 3]
    digit_2_values = [1, 9, 7, 1]
    linked_digit_1 = linked_list_from_array(digit_1_values)
    linked_digit_2 = linked_list_from_array(digit_2_values)
    print_linked_list(linked_digit_1)
    print_linked_list(linked_digit_2)
    print_linked_list(sum_linked(linked_digit_1, linked_digit_2))
