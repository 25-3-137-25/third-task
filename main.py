from caesar import *
from atbash import *
class ces:
    caesar = Caesar(shift=2)

    def __init__(self, text):
        self.original = text
        self.caesar = text


if __name__ == "__main__":
    print("write a message for a caesar encrypting (only in english)")
    j = str(input())
    msg = ces(j)
    print("Оригинал: ", msg.original)
    print("шифровка цезарем (на 2 символа): ", msg.caesar)


    decrypted = ces.caesar.decrypt(msg.caesar)
    print("дешифровка цезарем: ", decrypted)



class atb:
    atbash = Atbash()

    def __init__(self, text):
        self.original = text
        self.atbash = text


if __name__ == "__main__":
    print("write a message for an atbash encrypting (only in english)")
    j = str(input())
    msg = atb(j)
    print("Оригинал:      ", msg.original)
    print("Атбаш шифр:    ", msg.atbash)


    decrypted = atb.atbash.decrypt(msg.atbash)
    print("Атбаш дешифр:  ", decrypted)