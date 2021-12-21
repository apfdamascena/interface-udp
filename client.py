import socket
from threading import Thread
from datetime import date


class ClientUDP:

    BUFFER_SIZE = 1024
    START_CONNECTION = "connecting"


    def __init__(self, port, gui):
        self.__udp_client_socket = socket.socket(family=socket.AF_INET, type= socket.SOCK_DGRAM)
        self.__server_adress_port = ('localhost', port)
        self.__gui = gui

    def listenning(self):
        background_thread_send = Thread(target=self.send_message)
        background_thread_receive = Thread(target=self.receive_message)

        self.__udp_client_socket.sendto(bytes(ClientUDP.START_CONNECTION, "utf-8"), self.__server_adress_port)
     
        background_thread_receive.start()
        background_thread_send.start()

    def send_message(self, *user_message):
        if len(user_message) > 0:
            if isinstance(user_message[0], str):
                self.__udp_client_socket.sendto(bytes(user_message[0],'utf-8'), self.__informations)
            else:
                self.__udp_client_socket.sendto(user_message[0], self.__informations)


    def receive_message(self):
        while True:
            self.__message, self.__adress = self.__udp_client_socket.recvfrom(ClientUDP.BUFFER_SIZE)
            self.__message = self.__message.decode('utf-8')
            try:
                self.__receive_all_file(self.__message)
                self.__gui.receive_and_show_image(self.__filename)
            except:
                self.__gui.receive_and_show_at_screen(self.__message)
                self.__make_informations(self.__message)

    def __receive_all_file(self, header):
        self.__filename, _ = header.split(':')
        file = open(self.__filename, 'wb')
        while self.__message:
            self.__message, self.__adress = self.__udp_client_socket.recvfrom(ClientUDP.BUFFER_SIZE)
            file.write(self.__message)
        file.close()
    
    def __make_informations(self, *information):
        information = information[0].strip()
        if information[0] == '(':
            information = eval(information)
            self.__informations = information
