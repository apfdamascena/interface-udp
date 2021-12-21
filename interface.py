from tkinter import *
from tkinter import filedialog
from client import ClientUDP
import pygame
from ImageScreen import ImageScreen
from ExtensionType import ExtensionType
from MessageCheck import MessageCheck

class GUI:
    def __init__(self, width, height):
        self.__window = Tk()
        self.__window.title('4 Atividade')
        self.__window.bind('<Return>', self.__send)

        self.__canva = Canvas(self.__window, width=width, height=height)
        self.__canva.grid(columnspan=3)

        self.__message_checker = MessageCheck()

        self.__createWidgets()

        self.__client = ClientUDP(28886, self)
        self.__client.listenning()

    def __createWidgets(self):
        self.__txt_area = Text(self.__canva, border=1)

        self.__txt_field = Entry(self.__canva, width=85, border=1, bg='white')
       
        self.__attachment = Button(self.__canva, text='Attachment', command=self.__open_dialog_with_files)
        self.__send_button = Button(self.__canva, text='Send', padx=40, command=self.__send)
        self.__audio_button = Button(self.__canva, text='Play Last Audio', padx=40, command=self.__play_audio)
        self.__clear_button = Button(self.__canva, text='Clear', padx=40, command=self.__clear)
        
        self.__send_button.grid(column=2, row=1)
        self.__clear_button.grid(column=3, row=1)
        self.__attachment.grid(column=4, row=1)
        self.__audio_button.grid(column=5,row=1)
        self.__txt_area.grid(column=0, row=0, columnspan=3)
        self.__txt_field.grid(column=0, row=1, columnspan=2)
        
        self.__txt_area.config(background='#abd3eb')

    def __open_dialog_with_files(self):
        image_on_screen = ImageScreen(self.__txt_area)
        filename = filedialog.askopenfilename()
        extension_type = ExtensionType()

        if extension_type.check_photo_extension(filename):
           image_on_screen.add(150, filename)           
        elif extension_type.check_video_extension(filename):
           image_on_screen.add(120) 
           self.__last_audio = filename
        self.__send_file(filename)
         
    def __send_file(self, filename):
        name = filename.split('/')[-1]
        header = f'{name}:file'
        self.__client.send_message(header)

        file = open(filename, 'rb')
        parts_bytes_file = True
        while parts_bytes_file:
            parts_bytes_file = file.read(ClientUDP.BUFFER_SIZE) 
            self.__client.send_message(parts_bytes_file)
        file.close()

    def __play_audio(self):
        pygame.init()
        pygame.mixer.music.load(self.__last_audio)
        pygame.mixer.music.play(loops=0)
    
    def receive_and_show_at_screen(self, message):
        if self.__message_checker.is_printable(message): 
            self.__txt_area.insert(END, f'Another User: {message}\n')
            self.__txt_field.delete(0, END)

    def __send(self, event=None):
        text = self.__message_checker.is_valid_input(self.__txt_field.get())
        self.__client.send_message(text)
        self.__txt_area.insert(END, f'You: {text}')
        self.__txt_field.delete(0, END)

    def __clear(self):
        self.__txt_area.delete('1.0', END)

    def start(self):
        self.__window.mainloop()
        

if __name__ == '__main__':
    interface = GUI(800, 600).start()
