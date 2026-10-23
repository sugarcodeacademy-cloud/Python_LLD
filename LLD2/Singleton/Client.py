from LLD2.Singleton.Problem2 import Database

# db1 = Database.create_instance()
# db2 = Database.create_instance()

db1 = Database()
db2 = Database()

print(db1 is db2) #Two instances are created