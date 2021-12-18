import socket
from abc import ABC, abstractmethod
import datetime
import pickle
from threading import Thread

class ServerUDP:

    BUFFER_SIZE = 1024

    def __init__(self, port):
        self.__udp_server_socket = socket.socket(family=socket.AF_INET, type= socket.SOCK_DGRAM)
        self.__udp_server_socket.bind(('localhost', port))
        self.__connections = []


    def listening(self):
        while True:
            self.__message_from_client, self.__client_adress = self.__udp_server_socket.recvfrom(ServerUDP.BUFFER_SIZE)
            self.__connections.append(self.__client_adress)

            if len(self.__connections) == 2:
                self.__udp_server_socket.sendto(bytes(f'{self.__connections[1]}','utf-8'), self.__connections[0])
                self.__udp_server_socket.sendto(bytes(f'{self.__connections[0]}','utf-8'), self.__connections[1])
                self.__connections = []
            else:
                self.__udp_server_socket.sendto(bytes(f'Waiting another user', 'utf-8'), self.__connections[0])


if __name__ == "__main__":
    server = ServerUDP(28886)
    server.listening()