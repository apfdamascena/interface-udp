from tkinter import *
from PIL import Image, ImageTk

class ImageScreen: 

    def __init__(self, text_area):
        self.__txt_area = text_area

    def add(self, size, filename=''):
        file = 'midia_teste/mp3.png' if filename == '' else filename
        file_pic = Image.open(file)
        miniature_pic = file_pic.resize((size, (size * file_pic.height) // file_pic.width), Image.ANTIALIAS)
        my_img = ImageTk.PhotoImage(miniature_pic)
        my_img.image = my_img 
        self.__txt_area.image_create(END, image=my_img)
        self.__txt_area.insert(END,f'\n')

