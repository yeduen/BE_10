class Eagle:
    def __init__(self, name, wingspan):
        self.name = name
        self.wingspan = wingspan  # cm 단위

    def sound(self):
        return "찍찍"

    def info(self):
        return f"{self.name} has a wingspan of {self.wingspan} cm and says {self.sound()}"