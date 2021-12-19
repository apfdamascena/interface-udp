import socket
from threading import Thread
from datetime import date


class ClientUDP:

    BUFFER_SIZE = 1024

    def __init__(self, port, gui):
        self.__udp_client_socket = socket.socket(family=socket.AF_INET, type= socket.SOCK_DGRAM)
        self.__server_adress_port = ('localhost', port)
        self.__counter = 1
        self.gui = gui

    def sending_message(self):
        background_thread_send = Thread(target=self.send_message)
        background_thread_receive = Thread(target=self.receive_message)

        self.__udp_client_socket.sendto(bytes("connecting", "utf-8"), self.__server_adress_port)
     
        background_thread_receive.start()
        background_thread_send.start()

    def send_message(self, *user_message):
        if len(user_message) > 0:
            self.__udp_client_socket.sendto(bytes(user_message[0],'utf-8'), (self.__informations[0], int(self.__informations[1])))

    def receive_message(self, *test):
        while True:
            self.__message, self.__adress = self.__udp_client_socket.recvfrom(ClientUDP.BUFFER_SIZE)
            self.gui.recive(self.__message)
            self.make_informations(self.__message)
    
    def make_informations(self, *information):
        information = information[0].decode('utf-8').strip()
        if information[0] == '(':
            information = eval(information)
            print(f'{information}\n')
            self.__informations = information
        else:
            print(f'Sender: {self.__adress[1]}\nDate: {date.today()}\nNumber Message: {self.__counter}\nMessage: {information}\n')
            self.__counter += 1
