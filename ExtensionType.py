from  TypeFile import TypeFile
class ExtensionType:

    def __init__(self):
        self.__photo_extension = ['jpg', 'jpeg', 'png'] 
        self.__video_extension = ['mp4']
        self.__audio_extension = ['mp3', 'wav', 'mpeg']

    def check_extension(self, filename):
        type = None 
        for extension in self.__photo_extension:
            if extension in filename:
                type = TypeFile.IMAGE
        
        for extension in self.__audio_extension:
            if extension in filename:
                type = TypeFile.AUDIO

        for extension in self.__video_extension:
            if extension in filename:
                type = TypeFile.VIDEO
        
        return type

