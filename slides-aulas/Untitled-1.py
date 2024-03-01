class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def remover_duplicatas(self):
        if not self.head or not self.head.next:
            return

        seen = set()
        current = self.head
        previous = None

        while current:
            if current.data in seen:
                previous.next = current.next
            else:
                seen.add(current.data)
                previous = current
            current = current.next

# Teste
linked_list = LinkedList()
values = [1, 2, 3, 2, 4, 5, 1, 6]

for value in values:
    linked_list.append(value)

print("Lista Original:")
linked_list.display()

linked_list.remover_duplicatas()

print("\nLista após Remoção de Duplicatas:")
linked_list.display()
