from LLD1.Day9.ConsumerProducer.Store import Store


class Consumer:
    def __init__(self, store):
        self.store = store

    def run(self):
        while True:
            if len(self.store.get_items()) > 0:
                self.store.remove_item()
            else:
                print("Zero grab")