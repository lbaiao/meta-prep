def parse_input(filename: str):
    with open(filename, 'r') as in_file:
        lines = in_file.readlines()
        n = int(lines[0].strip())
        linked_list = [int(i.strip()) for i in lines[1:n+1]]
        data = int(lines[-2].strip())
        position = int(lines[-1].strip())
        return (n, linked_list, data, position)


class SinglyLinkedListNode:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class SinglyLinkedList:
    head: SinglyLinkedListNode

    def __init__(self):
        self.head = None
    
    def append(self, data: int):
        node = SinglyLinkedListNode(data)

        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = node

    def print(self):
        current = self.head
        print(current.data)
        while current.next != None:
            current = current.next
            print(current.data)        


def print_llist(llist:SinglyLinkedList):
    current = llist.head
    print(current.data)
    while current.next != None:
        current = current.next
        print(current.data)        

def insert_node_at_position(llist: SinglyLinkedList, data: int, position: int):
    current = llist.head
    node = SinglyLinkedListNode(data)

    if position == 0:
        node.next = llist.head
        llist.head = node
        return llist.head

    for _ in range(position - 1):
        if (current is None):
            raise Exception('Invalid position.')
        current = current.next

    node.next = current.next
    current.next = node

    return llist.head


if __name__ == '__main__':
    (n, llist, data, position) = parse_input('./input.txt')

    lk_list = SinglyLinkedList()
    for lt in llist:
        lk_list.append(lt)

    print(insert_node_at_position(lk_list, data, position))
    lk_list.print()

