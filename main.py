# main.py

from caesar import *

class Message:
    caesar = Caesar(shift=2)

    def __init__(self, text):
        self.original = text
        self.caesar = text


if __name__ == "__main__":
    print("only english")
    j = str(input())
    msg = Message(j)
    print("Оригинал: ", msg.original)
    print("шифровка цезарем (на 2 символа): ", msg.caesar)


    decrypted = Message.caesar.decrypt(msg.caesar)
    print("дешифровка цезарем: ", decrypted)
