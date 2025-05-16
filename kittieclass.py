# From the 'Virtual Pets' task set in software engineering
class Kittie:
    def __init__(self, name):
        self.name = name
        self.age = 0
        self.hunger = 0
        self.boredom = 0
        self.sleepy = 0
        self.dead = False

# Methods
    def stats(self):
        print("These are {self.name}'s current stats:")
        print(f'Age: {self.age}')
        print(f'Hunger: {self.hunger}/5')
        print(f'Boredom: {self.boredom}/5')
        print(f'Sleepiness: {self.sleepy/5}')

    def feed(self):
        self.hunger = self.hunger - 3
        if self.hunger < 0:
            self.hunger = 0\
    
    def play(self):
        self.boredom = self.boredom - 3
        if self.boredom < 0:
            self.boredom = 0

    def sleep(self):
        self.sleepy = self.sleepy - 3
        if self.sleepy < 0:
            self.sleepy = 0