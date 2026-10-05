import multiprocessing,os


# def print_student():
#     name = "Vinod"
#     number = 34
#     age = 29
#     email = "vinod@sugarcode.com"
#     # print("Name :" , name, "age :" , age, "email :" , email, "number :" , number)
#     # print(f"Name : {name} , age: {age} , email: {email} , number : {number}") #f string

def print_process_id():
    print(f"Process ID: {os.getpid()}")

if __name__ == '__main__':
    print_process_id()
    process = multiprocessing.Process(target=print_process_id)
    process.start()