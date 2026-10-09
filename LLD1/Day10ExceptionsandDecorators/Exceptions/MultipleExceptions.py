from LLD1.Day10ExceptionsandDecorators.Exceptions.CustomException.ValueException import ValueException


def divide(a,b):
    if b < 0:
        raise ValueException("cannot divide with values less than zero")
    print(("Hello"))
    return a/b

# try:
#     print(divide(10, 0))
# except (TypeError, ZeroDivisionError, Exception) as e:
#     print(f"Error: {e}")

#if your logic is different for  multiple error

try:
    print(divide(10, 2))
except TypeError as e:
    print("type error")
except ZeroDivisionError as e:
    print("Zero Division error")
finally:
    print("Finally block is executed if function is working or exception is thrown")

#connect to db
# try:
#     fetch the data from the db
# except Exception as e:
#    no data, no permissions, connection loss
# finally:
#     close the connection to the DB



print("Hello")
