from tkinter import *
from tkinter import filedialog
from datetime import datetime
from PIL import Image, ImageTk
import pygame
from tkvideo import tkvideo

class GUI:
    def __init__(self, width, height):
        self.window = Tk()
        self.window.title('4 Atividade')

        self.canva = Canvas(self.window, width=width, height=height)
        self.canva.grid(columnspan=3)
        #self.window.geometry(f"{width}x{height}")
        
        self.createWidgets()
        self.__bind()

    def __bind(self): 
        self.window.bind('<Return>', self.send)

    def createWidgets(self):
        self.txt_area = Text(self.canva, border=1)
        self.audio_button = Button(self.canva, text='Play Last Audio', padx=40, command=self.play_audio)
        self.txt_field = Entry(self.canva, width=85, border=1, bg='white')
        self.send_button = Button(self.canva, text='Send', padx=40, command=self.send)
        self.attachment = Button(self.canva, text='Attachment', command=self.open_dialog_with_files)
        self.clear_button = Button(self.canva, text='Clear', padx=40, command=self.clear)

        self.txt_area.config(background='#abd3eb')
        
        self.txt_area.grid(column=0, row=0, columnspan=3)
        self.audio_button.grid(column=5,row=1)
        self.txt_field.grid(column=0, row=1, columnspan=2)
        self.send_button.grid(column=2, row=1)
        self.clear_button.grid(column=3, row=1)
        self.attachment.grid(column=4, row=1)

        
        
    def open_dialog_with_files(self):
        filename = filedialog.askopenfilename()
        if filename[-3:] == 'jpg' or filename[-4:] == 'jpeg' or filename[-3:] == 'png': # caso seja uma imagem jpg ou jpeg vai exibir elas
            file_pic = Image.open(filename)
            miniature_pic = file_pic.resize((150, (150*file_pic.height)//file_pic.width), Image.ANTIALIAS)
            
            my_img = ImageTk.PhotoImage(miniature_pic)
            
            my_img.image = my_img #cria uma referência, evita que o coletor de lixo do python dê problema.
            self.txt_area.image_create(END, image=my_img)
            self.txt_area.insert(END,f'\n') #serve apenas pra próxima imagem não bugar e aparecer na lateral 
        
        elif filename[-3:] == "wav" or filename[-3:] == 'mp3': #reproduz música
            
            #exibe o ícone do mp3
            file_pic = Image.open('mp3.png')
            miniature_pic = file_pic.resize((120, (120*file_pic.height)//file_pic.width), Image.ANTIALIAS)
            my_img = ImageTk.PhotoImage(miniature_pic)
            my_img.image = my_img 
            self.txt_area.image_create(END, image=my_img)
            self.txt_area.insert(END,f'\n')
            
            self.last_audio = filename 
            
            
        '''elif filename[-3:] == 'mp4':
            player = tkvideo(filename, self.window ,loop = 1, size = (700, 500))
            player.play()'''
    
    
    
    def play_audio(self):
            pygame.init()
            pygame.mixer.music.load(self.last_audio)
            pygame.mixer.music.play(loops=0)
        
        
        
    

    def send(self, event=None):
        text = self.check_valid_input(self.txt_field.get())
        self.txt_area.insert(END, text)
        self.txt_field.delete(0, END)

    def check_valid_input(self, user_input):
        if user_input.strip() == '':
            return 'Invalid message! Please, try again \n'
        else:
            now = datetime.now()
            return f'{[now.strftime("%H:%M:%S")]} {self.txt_field.get()}\n'

    def clear(self):
        self.txt_area.delete('1.0', END)

    def start(self):
        self.window.mainloop()
        

if __name__ == '__main__':
    interface = GUI(800, 600).start()