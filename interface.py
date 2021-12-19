from tkinter import *
from tkinter import filedialog
from datetime import datetime
from client import ClientUDP
from PIL import Image, ImageTk


class GUI:
    def __init__(self, width, height):
        self.__window = Tk()
        self.__window.title('4 Atividade')
        self.__window.bind('<Return>', self.__send)

        self.__canva = Canvas(self.__window, width=width, height=height)
        self.__canva.grid(columnspan=3)
        
        self.__createWidgets()
  
        self.__client = ClientUDP(28886, self)
        self.__client.sending_message()
        
    def __createWidgets(self):
        self.__txt_area = Text(self.__canva, border=1)

        self.__txt_field = Entry(self.__canva, width=85, border=1, bg='white')
        self.__send_button = Button(self.__canva, text='Send', padx=40, command=self.__send)
        self.__attachment = Button(self.__canva, text='Attachment', command=self.__open_dialog_with_files)
        self.__clear_button = Button(self.__canva, text='Clear', padx=40, command=self.__clear)

        self.__txt_area.config(background='#abd3eb')
        
        self.__txt_area.grid(column=0, row=0, columnspan=3)
        
        self.__txt_field.grid(column=0, row=1, columnspan=2)
        self.__send_button.grid(column=2, row=1)
        self.__clear_button.grid(column=3, row=1)
        self.__attachment.grid(column=4, row=1)

    def __open_dialog_with_files(self):
        filename = filedialog.askopenfilename()
        file_pic = Image.open(filename)
        miniature_pic = file_pic.resize((150, (150*file_pic.height)//file_pic.width), Image.ANTIALIAS)
        
        my_img = ImageTk.PhotoImage(miniature_pic)    
        
        my_img.image = my_img # cria uma referência, evita que o coletor de lixo do python dê problema.
        
        self.__txt_area.image_create(END, image=my_img)
        self.__txt_area.insert(END,f'\n') # serve apenas pra próxima imagem não bugar e aparecer na lateral
    
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
