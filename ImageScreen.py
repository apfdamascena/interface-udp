from tkinter import *
from PIL import Image, ImageTk

class ImageScreen: 

    def __init__(self, text_area):
        self.__txt_area = text_area

    def add(self, type_file, filename):
        possibles = [filename, 'midia_teste/mp4.png', 'midia_teste/mp3.png']
        file = possibles[type_file]
        file_pic = Image.open(file)
        miniature_pic = file_pic.resize((120, (120 * file_pic.height) // file_pic.width), Image.ANTIALIAS)
        my_img = ImageTk.PhotoImage(miniature_pic)
        my_img.image = my_img 
        self.__txt_area.image_create(END, image=my_img)
        self.__txt_area.insert(END,f'\n')
        self.__txt_area.insert(END,f'\n')

