class linked_node:
    def __init__(self, data, next):
        self.data = data
        self.next = next


def has_cycle(head: linked_node):
    addresses = []
    current = head
    addresses.append(id(current))
    while current.next != None:
        if id(current.next) in addresses:
            return 1
        else:
            addresses.append(id(current.next))
            current = current.next

    return 0

x = 'lucas'
print(id(x))
