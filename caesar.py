class Caesar:
    def __init__(self, shift=2):
        self.shift = shift
        self.private_name = None

    def __set_name__(self, owner, name):

        self.private_name = "_" + name

    def __get__(self, instance, owner=None):
        if instance is None:
            return self

        return getattr(instance, self.private_name, "")

    def __set__(self, instance, value):

        text = str(value)
        res = ""
        for ch in text:
            if "a" <= ch <= "z":

                pos = ord(ch) - ord("a")
                pos = (pos + self.shift) % 26
                res += chr(ord("a") + pos)
            else:
                res += ch

        setattr(instance, self.private_name, res)


    def decrypt(self, text):
        res = ""
        for ch in text:
            if "a" <= ch <= "z":
                pos = ord(ch) - ord("a")
                pos = (pos - self.shift) % 26
                res += chr(ord("a") + pos)
            else:
                res += ch
        return res
