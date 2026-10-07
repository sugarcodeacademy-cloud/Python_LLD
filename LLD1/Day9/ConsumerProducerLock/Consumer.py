from LLD1.Day9.ConsumerProducer.Store import Store


class Consumer:
    def __init__(self, store,lock):
        self.store = store
        self.store_lock = lock

    def run(self):
        while True:
            with self.store_lock:
                if len(self.store.get_items()) > 0:
                    self.store.remove_item()