
class Atbash:
    def __init__(self):
        self.private_name = None

    def __set_name__(self, owner, name):
        self.private_name = "_" + name

    def __get__(self, instance, owner=None):
        if instance is None:
            return self
        return instance.__dict__.get(self.private_name, "")

    def __set__(self, instance, value):
        text = str(value)
        res = ""
        for ch in text:
            if "a" <= ch <= "z":
                pos = ord(ch) - ord("a")
                pos = 25 - pos
                res += chr(ord("a") + pos)
            else:
                res += ch
        instance.__dict__[self.private_name] = res


    def decrypt(self, text):
        res = ""
        for ch in text:
            if "a" <= ch <= "z":
                pos = ord(ch) - ord("a")
                pos = 25 - pos
                res += chr(ord("a") + pos)
            else:
                res += ch
        return res
