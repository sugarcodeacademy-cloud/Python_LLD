from LLD1.Day9.ConsumerProducer.Store import Store


class Producer:
    def __init__(self,store,lock):
        self.store = store
        self.store_lock = lock

    def run(self):
        while True:
            with self.store_lock:
                if len(self.store.get_items())< self.store.get_max_size():
                    self.store.add_item(object())
