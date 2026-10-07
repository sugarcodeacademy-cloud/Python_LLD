

from LLD1.Day9.ConsumerProducerLock.Consumer import Consumer
from LLD1.Day9.ConsumerProducerLock.Producer import Producer
from LLD1.Day9.ConsumerProducerLock.Store import Store

from threading import RLock, Thread
store = Store(10)
lock = RLock()

#Hire 8 producers
for i in range(8):
    producer = Producer(store, lock)
    Thread(target = producer.run, name= f"Producer - {i}").start()

#Oper door for 20 consumers
for i in range(20):
    consumer = Consumer(store, lock)
    Thread(target=consumer.run,name = f"Consumer - {i}").start()
