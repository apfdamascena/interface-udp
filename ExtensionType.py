class ExtensionType:

    def __init__(self):
        self.__photo_extension = ['jpg', 'jpeg', 'png'] 
        self.__video_extension = ['wav', 'mp3']

    def check_photo_extension(self, filename):
        for extension in self.__photo_extension:
            if filename.endswith(extension):
                return True
        return False

    def check_video_extension(self, filename):
        for extension in self.__video_extension:
            if filename.endswith(extension):
                return True
        return False

