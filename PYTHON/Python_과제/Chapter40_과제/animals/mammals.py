class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def sound(self):
        return "왈왈!"

    def info(self):
        return f"{self.name} is a {self.breed} and says {self.sound()}"