import threading

from LLD1.Day9.ConsumerProducerSemaphore.Consumer import Consumer
from LLD1.Day9.ConsumerProducerSemaphore.Producer import Producer
from LLD1.Day9.ConsumerProducerSemaphore.Store import Store


store = Store(8)
producer_semaphore  = threading.Semaphore(8) #7 8

consumer_semaphore = threading.Semaphore(0) #1 0

#Hire 8 producers
for i in range(8):
    producer = Producer(store, producer_semaphore , consumer_semaphore , i)
    threading.Thread(target = producer.run).start()

#Oper door for 20 consumers
for i in range(20):
    consumer = Consumer(store, consumer_semaphore,producer_semaphore, i)
    threading.Thread(target=consumer.run).start()
