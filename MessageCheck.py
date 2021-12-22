from datetime import datetime

class MessageCheck:

    def __init__(self):
        self.__non_printable = ['Waiting another user', 'Invalid message! Please, try again']

    def is_printable(self, message):
        return not ((message.strip() in self.__non_printable) or (message[0] == '(' and message[-1] == ')'))

    def is_valid_input(self, from_user_input):
        if not from_user_input.strip():
            return 'Invalid message! Please, try again \n'
        now = datetime.now()
        return f'{[now.strftime("%H:%M:%S")]} {from_user_input}\n'


        