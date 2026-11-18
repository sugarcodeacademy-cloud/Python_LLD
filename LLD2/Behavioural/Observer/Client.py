from LLD2.Behavioural.Observer.User import User
from LLD2.Behavioural.Observer.YouTubeChannel import YouTubeChannel


class YouTube():
    user1 = User("Rahul", "xyz@abc.com", "Rahul")
    user2 = User("Bhavya", "abc@xyz.com", "Bhavya")
    user3 = User("Vinod", "abcdef@xyz.com", "Vinod")

    sugarCodeChannel = YouTubeChannel()

    sugarCodeChannel.subscribe(user1)
    sugarCodeChannel.subscribe(user2)

    sugarCodeChannel.upload_video("New Python Class has been added")
    print("___________________________________")

    sugarCodeChannel.unscribe(user2)

    sugarCodeChannel.upload_video("New AI tool has been launched")
    print("-------------------------------------------------")

    AIVerseChannel = YouTubeChannel()

    AIVerseChannel.subscribe(user3)

    AIVerseChannel.upload_video("New data leak has happened by claude ")

