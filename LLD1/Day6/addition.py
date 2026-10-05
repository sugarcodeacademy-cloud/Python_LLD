#prior to python 3
def add(a, b):
    return a+b

print(add(3,4))
print(add("Hi", " Hello"))
# #print(add(3, " Hi"))
# print(add([1,2,3], [4,5,6]))
# print(add[1,2,3], 4)

def add1(a:int, b:int)-> int :
    #type hints
    return a+b

print(add1(2,3))
# print(add1("Hi", "Hello"))

#def function_name(parameter_name: Type of the paramater) -> ReturnType:
