class PostgressTransaction():
    def begin(self):
        print("[Postgress] Starting session and transaction")

    def commit(self):
        print("[Postgress] Committing transaction")

    def rollback(self):
        print("[Postgress] Aborting transaction")