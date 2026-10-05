#Instating the Thread class
# from threading import Thread
#
# def print_str():
#     print("Thread is running")
#
# #create a thread using a Thread function
# my_thread = Thread(target=print_str)
#
# #starting the thread
# my_thread.start()
#
# #waiting for thread to complete
# my_thread.join()


#extending Thread class
from threading import Thread
class MyThread(Thread):
    def run(self):
        print("Thread function is running")

my_thread = MyThread()

my_thread.start()

my_thread.join()

