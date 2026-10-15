# class Database:
#     _instance = None
#     def __init__(self):
#         if self._intialized:
#             return
#         self._intialized = True
#         print("Database is connecting ")
#
#     # @staticmethod
#     # def create_instance():
#     #     if Database._instance is None:
#     #         Database._instance = Database()
#     #     return Database._instance
#
#     # @classmethod
#     # def create_instance(cls):
#     #     if cls._instance is None:
#     #         cls._instance = super().__new__(cls)
#     #     return cls._instance
#
#     def __new__(cls):
#         if cls._instance is None:
#             cls._instance = super().__new__(cls)
#             cls._instance._intialized = False
#         return cls._instance
