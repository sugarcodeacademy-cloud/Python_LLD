from LLD2.Factory import DatabaseSelector


class UserService:
    def __init__(self, user_selected_db):
        # self.mySqlDatabase = MySQLDatabase()
        self.db = DatabaseSelector.get_database(user_selected_db)
        self.dbf = self.db.create_database_factory()


    def create_user(self, name , email):
        q = self.dbf.createQuery("INSERT INTO users VALUES ('" + name + "', '" + email + "')");
        q.execute();
        print("User created: ", name)

    def update_user(self, name, new_email):
        txn = self.dbf.createTransaction()
        txn.begin()

        q = self.db.createQuery("UPDATE users SET email = '" + new_email + "' WHERE name='" + name + "'");
        self.db.execute();

        txn.commit()
        print(f"User updated: {name} --> {new_email}")
