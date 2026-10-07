from LLD1.Day9.ConsumerProducer.Store import Store


class Producer:
    def __init__(self,store):
        self.store = store

    def run(self):
        while True:
            if len(self.store.get_items())< self.store.get_max_size():
                self.store.add_item(object())
            else:
                print("Over Stocking")