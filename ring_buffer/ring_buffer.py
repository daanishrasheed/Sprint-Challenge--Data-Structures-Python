from bst import DoublyLinkedList

class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if len(self.storage) < self.capacity:
            self.storage.add_to_tail(item)
            self.current = self.storage.tail
            return
        elif self.current == self.storage.tail:
            self.current = self.storage.head
        else:
            self.current = self.current.next
        self.current.value = item

    def get(self):
        list_buffer_contents = []
        node = self.storage.head
        while node is not None:
            list_buffer_contents.append(node.value)
            node = node.next
        return list_buffer_contents