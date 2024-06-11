class STYLE:
    def __init__(self, name):
        self.f = open(name, 'r')

    def __str__(self):
        return self.f.read()

