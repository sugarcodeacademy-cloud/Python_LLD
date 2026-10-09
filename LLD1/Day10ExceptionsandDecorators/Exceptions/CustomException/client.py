from LLD1.Day10ExceptionsandDecorators.Exceptions.CustomException.ValueException import ValueException


def divide(a,b):
    if b < 0:
        raise ValueException("cannot divide with values less than zero")
    return a/b

try:
    print(divide(10, -2))
except ValueException as e:
    print(f"Error: {e}")
# print(divide(10, -2)) #code will stop working here


#advantages of try except
#1.not showing traceback to the users
#2.code doesn't stop executing after the exception
print("Hello")

