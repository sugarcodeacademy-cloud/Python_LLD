from LLD2.Behavioural.Observer.Channel import Channel


class YouTubeChannel(Channel):
    # users = []
    # def uploadVideo(self, vidoe_name):
    #     for user in users:
    #         notifyUser("New video has been uploaded ")
    def __init__(self):
        self.subscriberList = []

    def subscribe(self, subscriber):
        self.subscriberList.append(subscriber)

    def unscribe(self, subscriber):
        self.subscriberList.remove(subscriber)

    def upload_video(self, video_name):
        print(f"new Video has been uploaded : {video_name}")
        self.notifyUsers(video_name)

    def notifyUsers(self, video_name):
        for subscriber in self.subscriberList:
            subscriber.update(video_name)

