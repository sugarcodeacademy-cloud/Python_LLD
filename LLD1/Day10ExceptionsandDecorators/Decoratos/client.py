def my_decorator(func):
    def wrapper():
        print("Welcome to Mc Donald's")
        func() #print_bill()
        print("Thanks for visting Mcdonalds")
    return wrapper



@my_decorator
def print_bill():#bill1
    print("Bill1")

print_bill()

# decorator = my_decorator(print_bill)
# decorator()

