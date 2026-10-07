from LLD1.Day9.ConsumerProducer.Store import Store


class Producer:
    def __init__(self,store, producer_semaphore, consumer_semaphore, id):
        self.store = store
        self.producer_semaphore = producer_semaphore
        self.consumer_semaphore = consumer_semaphore
        self.id = id

    def run(self):
        while True:
            self.producer_semaphore.acquire()
            if len(self.store.get_items())< self.store.get_max_size():
                self.store.add_item(self.id)
            self.consumer_semaphore.release()
