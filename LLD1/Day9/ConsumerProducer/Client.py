import threading

from LLD1.Day9.ConsumerProducer.Consumer import Consumer
from LLD1.Day9.ConsumerProducer.Producer import Producer
from LLD1.Day9.ConsumerProducer.Store import Store


store = Store(10)

#Hire 8 producers
for i in range(25):
    producer = Producer(store)
    threading.Thread(target = producer.run).start()

#Oper door for 20 consumers
for i in range(20):
    consumer = Consumer(store)
    threading.Thread(target=consumer.run).start()
