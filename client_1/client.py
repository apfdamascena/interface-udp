import socket
from threading import Thread
from datetime import date


class ClientUDP:

    BUFFER_SIZE = 1024

    def __init__(self, port):
        self.__udp_client_socket = socket.socket(family=socket.AF_INET, type= socket.SOCK_DGRAM)
        self.__server_adress_port = ('localhost', port)
        self.__counter = 1


    def sending_message(self):
        background_thread_send = Thread(target= self.__send_message)
        background_thread_receive = Thread(target= self.__receive_message)

        self.__udp_client_socket.sendto(bytes("connecting", "utf-8"), self.__server_adress_port)
     
        background_thread_receive.start()
        background_thread_send.start()
       

    def __send_message(self):
        while True:
            message = input() 
            self.__udp_client_socket.sendto(bytes(message,'utf-8'), (self.__informations[0], int(self.__informations[1])))

    def __receive_message(self):
        while True:
            self.__message, self.__adress = self.__udp_client_socket.recvfrom(ClientUDP.BUFFER_SIZE)
            self.make_informations(self.__message)
    
    def make_informations(self, *information):
        information = information[0].decode('utf-8').strip()
        if information[0] == '(':
            helper = ""
            informations = []
            for letter in information:
                if letter == " " or letter == '(' or letter == ')' or letter == "'":
                    continue
                if letter != ',':
                    helper += letter
                else:
                    informations.append(helper)
                    helper = ""
            informations.append(helper)
            print(information)
            print()
            self.__informations = informations
        else:
            print(f'Sender: {self.__adress[1]}\nDate: {date.today()}\nNumber Message: {self.__counter}\nMessage: {information}\n')
            self.__counter += 1
                
                    
if __name__ == "__main__":
    client = ClientUDP(28886)
    client.sending_message()