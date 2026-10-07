import threading
from collections import deque


class Store:

    def __init__(self, capacity):
        self.capacity = capacity
        self.items = deque()
        self.print_lock = threading.RLock()

    def get_items(self):
        return self.items

    def add_item(self, id):
        self.items.append(object())
        with self.print_lock:
            print(
                "Producer added item. "
                "Current size:", len(self.items),
                "By Producer:", id
            )

    def remove_item(self, id):
        self.items.pop()
        with self.print_lock:
            print(
                "Consumer removed item. "
                "Current size:", len(self.items),
                "By Consumer:", id
            )

    def get_max_size(self):
        return self.capacity
