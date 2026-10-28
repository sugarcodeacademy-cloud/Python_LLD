from abc import abstractmethod, ABC

from LLD2.Factory.POSTGRESS.PostGressDatabase import PostGressDatabase
from LLD2.Factory.DatabaseType import DatabaseType
from LLD2.Factory.MYSQL.MySQLDatabase import MySQLDatabase


class DatabaseSelector(ABC):
    @abstractmethod
    def get_database(self, db):
        if db == DatabaseType.MY_SQL:
            return MySQLDatabase()
        elif db == DatabaseType.POST_GRESS:
            return PostGressDatabase()
        else:
            return None