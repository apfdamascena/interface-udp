from tkinter import *
from tkinter import filedialog
from datetime import datetime
from client import ClientUDP


class GUI:
    def __init__(self, width, height):
        self.window = Tk()
        self.window.title('4 Atividade')

        self.canva = Canvas(self.window, width=width, height=height)
        self.canva.grid(columnspan=3)
        self.createWidgets()
        self.__bind()

        self.client = ClientUDP(28886)
        self.client.sending_message()

    def __bind(self): 
        self.window.bind('<Return>', self.send)

    def createWidgets(self):
        self.txt_area = Text(self.canva, border=1)
        self.txt_field = Entry(self.canva, width=85, border=1, bg='white')
        self.send_button = Button(self.canva, text='Send', padx=40, command=self.send)
        self.attachment = Button(self.canva, text='Attachment', command=self.open_dialog_with_files)
        self.clear_button = Button(self.canva, text='Clear', padx=40, command=self.clear)
        
        self.txt_area.config(background='#abd3eb')

        self.txt_area.grid(column=0, row=0, columnspan=3)
        self.txt_field.grid(column=0, row=1, columnspan=2)
        self.send_button.grid(column=2, row=1)
        self.clear_button.grid(column=3, row=1)
        self.attachment.grid(column=4, row=1)

    def open_dialog_with_files(self):
        filename = filedialog.askopenfilename()
        my_image = PhotoImage(file=filename)
        self.txt_area.image_create(END, image = my_image)

    def send(self, event=None):
        text = self.check_valid_input(self.txt_field.get())
        self.txt_area.insert(END, text)
        self.client.send_message(text)
        self.txt_field.delete(0, END)

    def check_valid_input(self, user_input):
        print(user_input)
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
    interface = GUI(600, 800).start()