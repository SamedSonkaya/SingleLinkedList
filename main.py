class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SingleLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
    def delete(self, data):
        node = self.head

        if node and node.data == data:
            self.head = node.next
            node = None
            return

        b_node = None
        while node and node.data != data:
            b_node = node
            node = node.next

        if node:
            b_node.next = node.next
            node = None
    def display(self):
        current = self.head
        while current:
            print(current.data, end=' -> ')
            current = current.next
        print()

# Test
if __name__ == "__main__":
    linked_list = SingleLinkedList()
    linked_list.append(6)
    linked_list.append(11)
    linked_list.append(4)
    linked_list.append(7)
    linked_list.append(12)
    linked_list.delete(12)
    linked_list.delete(4)
    linked_list.display()