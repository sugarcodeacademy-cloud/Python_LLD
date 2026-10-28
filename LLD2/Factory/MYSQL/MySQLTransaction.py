from LLD2.Factory.Transaction import Transaction


class MySQLTransaction(Transaction):
    def begin(self):
        print("[MySQL] Starting session and transaction")

    def commit(self):
        print("[MySQL] Committing transaction")

    def rollback(self):
        print("[MySQL] Aborting transaction")
