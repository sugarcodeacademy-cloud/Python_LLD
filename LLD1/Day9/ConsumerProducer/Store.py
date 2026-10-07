class Store:
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = []

    def add_item(self, item):
        self.items.append(item)
        print("Producer added item. Current size : ", len(self.items))

    def remove_item(self):
        self.items.pop(0)
        print("Consumer bought the item, Current size: ", len(self.items))

    def get_items(self):
        return self.items

    def get_max_size(self):
        return self.capacity