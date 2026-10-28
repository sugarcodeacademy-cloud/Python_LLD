from LLD2.Factory.Query import Query


class MySQLQuery(Query):
    def execute(self, queryString):
        print(f"[MySQL] Executing SQL query: {queryString}")