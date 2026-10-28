from LLD2.Factory.DatabaseType import DatabaseType
from LLD2.Factory.UserService import UserService


class Client:
    # user_service = UserService()
    # user_service.create_user("Vinod", "abc@gmail.com")

    # mysql_database = MySQLDatabase()
    # user_service = UserService(mysql_database)
    # user_service.create_user("Vinod", "abc@gmail.com")

    user_service = UserService(DatabaseType.MY_SQL)
    user_service.create_user("Vinod", "abc@gmail.com")

    user_service_2 = UserService(DatabaseType.POST_GRESS)
    user_service_2.create_user("Bhavya", "qer@gmail.com")