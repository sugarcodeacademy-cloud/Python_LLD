from LLD2.Behavioural.Observer.Subscriber import Subscriber


class User(Subscriber):
    def __init__(self, name, email, profile_name):
        self.name = name
        self.email = email
        self.profile_name = profile_name

    def update(self, video_name):
        print(f"{self.profile_name} has a new video to watch {video_name}")