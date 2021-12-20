from tkinter import *
from tkinter import filedialog
from datetime import datetime
from client import ClientUDP
from PIL import Image, ImageTk
import pygame
from tkVideoPlayer import TkinterVideo


class GUI:
    def __init__(self, width, height):
        self.__window = Tk()
        self.__window.title('4 Atividade')
        self.__window.bind('<Return>', self.__send)

        self.__canva = Canvas(self.__window, width=width, height=height)
        self.__canva.grid(columnspan=3)
        
        self.__createWidgets()
        
       
        self.__contvideo = 0
        self.__contaudio = 0
        self.__client = ClientUDP(28886, self)
        self.__client.sending_message()

    def __createWidgets(self):
        self.__txt_area = Text(self.__canva, border=1)

        self.__txt_field = Entry(self.__canva, width=85, border=1, bg='white')
       
        self.__attachment = Button(self.__canva, text='Attachment', command=self.__open_dialog_with_files)
        self.__send_button = Button(self.__canva, text='Send', padx=40, command=self.__send)
        self.__audio_button = Button(self.__canva, text='Play Audio', padx=40, command=self.__play_audio)
        self.__video_button = Button(self.__canva, text='Play Video', padx=40, command=self.__play_video)
        self.__clear_button = Button(self.__canva, text='Clear', padx=40, command=self.__clear)

        self.__listaudio = Listbox(selectmode = SINGLE, width = 30)
        self.__listvideo = Listbox(selectmode = SINGLE, width = 30)
        self.__listvideo.grid(column=1, row=0, columnspan=3)
        self.__listaudio.grid(column=2, row=0, columnspan=2)
        
        self.__send_button.grid(column=2, row=1)
        self.__clear_button.grid(column=3, row=1)
        self.__attachment.grid(column=4, row=1)
        self.__audio_button.grid(column=5,row=1)
        self.__video_button.grid(column=6,row=1)
        self.__txt_area.grid(column=0, row=0, columnspan=3)
        self.__txt_field.grid(column=0, row=1, columnspan=2)
        
        self.__txt_area.config(background='#abd3eb')

    def __open_dialog_with_files(self):
        filename = filedialog.askopenfilename()
        if filename[-3:] == 'jpg' or filename[-4:] == 'jpeg' or filename[-3:] == 'png': # caso seja uma imagem jpg ou jpeg vai exibir elas
           #exibe a foto escolhida
           self.file_pic = Image.open(filename)
           self.miniature_pic = self.file_pic.resize((150, (150 * self.file_pic.height) // self.file_pic.width), Image.ANTIALIAS)
           self.my_img = ImageTk.PhotoImage(self.miniature_pic)
           self.my_img.image = self.my_img 
           
           self.__txt_area.image_create(END, image=self.my_img)
           self.__txt_area.insert(END,f'\n') #serve apenas pra próxima imagem não bugar e aparecer na lateral 
       
        elif filename[-3:] == "wav" or filename[-3:] == 'mp3': #caso seja uma música
           
           #exibe o ícone do mp3 simbolizando um áudio
            self.file_pic = Image.open('midia_teste/icone_mp3.png')
            self.miniature_pic = self.file_pic.resize((120, (120 * self.file_pic.height) // self.file_pic.width), Image.ANTIALIAS)
            self.my_img = ImageTk.PhotoImage(self.miniature_pic)
            self.my_img.image = self.my_img 
            
            self.__txt_area.image_create(END, image=self.my_img)
            self.__txt_area.insert(END,f'\n')

            self.__listaudio.insert(self.__contaudio,filename)
            self.__contaudio +=1
        
        elif filename[-3:] == 'mp4': #caso seja um video
            #exibe o símbolo para representar um vídeo
            self.file_pic = Image.open('midia_teste/icone_video.png')
            self.miniature_pic = self.file_pic.resize((120, (120 * self.file_pic.height) // self.file_pic.width), Image.ANTIALIAS)
            self.my_img = ImageTk.PhotoImage(self.miniature_pic)
            self.my_img.image = self.my_img 
            
            self.__txt_area.image_create(END, image=self.my_img)
            self.__txt_area.insert(END,f'\n')
            
            self.__listvideo.insert(self.__contvideo,filename)
            self.__contvideo +=1
            

    
    def __play_video(self):
        temp = self.__txt_area
        video_escolhido = self.__listvideo.get(self.__listvideo.curselection())
        
        newwindow = Toplevel(self.__window)
        newwindow.title("Videoplayer")
        newwindow.geometry("600x400")
        Label(newwindow).pack(anchor = 'center')
        
        
        self.videoplayer = TkinterVideo(master=newwindow, scaled = True, pre_load=True)
        self.videoplayer.set_size((400,250))
        self.videoplayer.load(video_escolhido)
        self.videoplayer.pack()
        self.videoplayer.play()
        
        
    
    def __play_audio(self):
        musica_escolhida = self.__listaudio.get(self.__listaudio.curselection())
        pygame.init()
        pygame.mixer.music.load(musica_escolhida)
        pygame.mixer.music.play(loops=0)
    
    def receive_and_show_at_screen(self, message):
        message = message.decode('utf-8').strip()
        non_printable = ['Waiting another user', 'Invalid message! Please, try again \n']
        if not ((message in non_printable) or (message[0] == '(' and message[-1] == ')')):
            self.__txt_area.insert(END, f'Another User: {message}\n')
            self.__txt_field.delete(0, END)

    def __send(self, event=None):
        text = self.__check_valid_input(self.__txt_field.get())
        self.__client.send_message(text)
        self.__txt_area.insert(END, f'You: {text}')
        self.__txt_field.delete(0, END)

    def __check_valid_input(self, user_input):
        if not user_input.strip():
            return 'Invalid message! Please, try again \n'
        else:
            now = datetime.now()
            return f'{[now.strftime("%H:%M:%S")]} {self.__txt_field.get()}\n'

    def __clear(self):
        self.__txt_area.delete('1.0', END)

    def start(self):
        self.__window.mainloop()
        

if __name__ == '__main__':
    interface = GUI(800, 600).start()
