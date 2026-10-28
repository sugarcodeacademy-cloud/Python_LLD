
from LLD2.Factory.DatabaseFactory import DatabaseFactory
from LLD2.Factory.POSTGRESS.PostgressQuery import PostgressQuery
from LLD2.Factory.POSTGRESS.PostgressTransaction import PostgressTransaction


class PostgressFactory(DatabaseFactory):
    def createQuery(self, query):
        return PostgressQuery(query)

    def createTransaction(self):
        return PostgressTransaction()