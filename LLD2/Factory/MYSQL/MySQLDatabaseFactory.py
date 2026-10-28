from LLD2.Factory.MYSQL.MySQLQuery import MySQLQuery
from LLD2.Factory.MYSQL.MySQLTransaction import MySQLTransaction
from LLD2.Factory.DatabaseFactory import DatabaseFactory


class MySQLDatabaseFactory(DatabaseFactory):
    def createQuery(self, query):
        return MySQLQuery(query)

    def createTransaction(self):
        return MySQLTransaction()