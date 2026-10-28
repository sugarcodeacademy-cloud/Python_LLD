from LLD2.Factory.Database import Database
from LLD2.Factory.POSTGRESS.PostgressFactory import PostgressFactory


class PostGressDatabase(Database):
    def connect(self):
        print(f"[Postgress] Connected to Postgress database")

    def change_pool_size(self, size):
        print(f"[Postgress] Pool size changed to {size}")

    def getVersion(self):
        return "Postgress 6.2"

    def create_database_factory(self):
        return PostgressFactory()