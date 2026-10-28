from abc import abstractmethod, ABC


class DatabaseFactory(ABC):
    # @abstractmethod
    # def get_database(db):
    #     if db == DatabaseType.MY_SQL:
    #         return MySQLDatabase()
    #     elif db == DatabaseType.POST_GRESS:
    #         return PostGressDatabase();
    #     else:
    #         return None;
    @abstractmethod
    def createQuery(self, sql):
        pass

    @abstractmethod
    def createTransaction(self):
        pass

