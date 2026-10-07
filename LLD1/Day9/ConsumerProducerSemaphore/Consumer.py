from LLD1.Day9.ConsumerProducer.Store import Store


class Consumer:
    def __init__(self, store, consumer_semaphore, producer_semaphore, id):
        self.store = store
        self.consumer_semaphore = consumer_semaphore
        self.producer_semaphore = producer_semaphore
        self.id = id

    def run(self):
        while True:
            self.consumer_semaphore.acquire()
            if len(self.store.get_items()) > 0:
                self.store.remove_item(self.id)
            self.producer_semaphore.release()
