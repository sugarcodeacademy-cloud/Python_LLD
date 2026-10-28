from LLD2.Factory.Database import Database
from LLD2.Factory.MYSQL.MySQLDatabaseFactory import MySQLDatabaseFactory


class MySQLDatabase(Database):
    def connect(self):
        print(f"[MySQL] Connected to MySQL database")

    def change_pool_size(self, size):
        print(f"[MySQL] Pool size changed to {size}")

    def getVersion(self):
        return "MYSQL 8.0"

    def create_database_factory(self):
        return MySQLDatabaseFactory()