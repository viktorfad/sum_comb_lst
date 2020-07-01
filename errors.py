class ArrayTypeError(Exception):
    def __init__(self, text):
        self.txt = text

class kTypeError(Exception):
    def __init__(self, text):
        self.txt = text

class NullValue(Exception):
    def __init__(self, text):
        self.txt = text
