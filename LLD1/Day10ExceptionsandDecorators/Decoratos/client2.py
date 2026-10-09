def my_decorator(func):
    def wrapper(*args,**kwargs):
        print("Welcome to Mc Donald's")
        result = func(*args, **kwargs) #print_bill()
        print(result)
        print("Thanks for visting Mcdonalds")
        # return result
    return wrapper

@my_decorator
def add(a, b):
    return a+b

add(10, 20)
