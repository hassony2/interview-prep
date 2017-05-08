from src.linkedlist import LinkListException, Node, print_online, linked_list_from_array


def detect_cycle(head):
    # Initialize pointers
    if(head.next):
        slow = head
        fast = head.next
    else:
        return None

    while(fast.next is not None):
        print(fast.data)
        fast = fast.next
        if(fast is slow):
            return fast
        if(fast.next is not None):
            fast = fast.next
            if(fast is slow):
                return fast
        else:
            return None
        slow = slow.next

def get_cycle_size(cycle_node):
    current_node = cycle_node
    counter = 0
    in_cycle = True
    while(in_cycle):
        current_node = current_node.next
        counter += 1
        if current_node is cycle_node:
            in_cycle = False
    return counter

def get_cycle_beginning(head, cycle_size):
    fwd_pointer = head
    back_pointer = head
    for i in range(cycle_size):
        fwd_pointer = fwd_pointer.next
    search = True
    while(search):
        if(fwd_pointer is back_pointer):
            search = False
        else:
            fwd_pointer = fwd_pointer.next
            back_pointer = back_pointer.next
    return back_pointer

if __name__ == "__main__":
    link_values = [0, 1, 2, 3, 4]
    link_list = linked_list_from_array(link_values)
    cycle_values = [5, 6, 7, 8]
    cycle_head = linked_list_from_array(cycle_values)
    link_list.next.next.next.next.next = cycle_head
    cycle_head.next.next.next.next = cycle_head

    # find node in cycle
    cycle_pointer = detect_cycle(link_list)
    if(cycle_pointer):
        print("found cycle !")

    # Find cycle size
    cycle_size = get_cycle_size(cycle_pointer)
    print(cycle_size)

    # Find cycle beginning
    fisrt_cycle_node = get_cycle_beginning(link_list, cycle_size)
    print(fisrt_cycle_node.data)