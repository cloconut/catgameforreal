# From the 'Virtual Pets' task set in software engineering

# Kittie Class

class Kittie:
    # Constructor
    def __init__(self, name):

# Attributes

        self.name = name # The name of the pet
        self.age = 0 # Age of the pet
        self.hunger = 0 # How hungry is the pet (0-5 scale)
        self.boredom = 0 # How bored is the pet (0-5 scale)
        self.sleepy = 0 # How sleepy is the pet (0-5 scale)
        self.dead = False # Is the pet dead?

# Methods

    # Prints the stats of the pet
    def stats(self): 
        print("These are {self.name}'s current stats:")
        print(f'Age: {self.age}')
        print(f'Hunger: {self.hunger}/5')
        print(f'Boredom: {self.boredom}/5')
        print(f'Sleepiness: {self.sleepy/5}')

     # Reduces hunger
    def feed(self):
        self.hunger = self.hunger - 3 # Reduce score by 3
        # If score reaches 0
        if self.hunger < 0: 
            self.hunger = 0
    
    # Reduces boredom
    def play(self):
        self.boredom = self.boredom - 3 # Reduce score by 3
        # If score reaches 0
        if self.boredom < 0:
            self.boredom = 0

    # Reduces sleepiness
    def sleep(self):
        self.sleepy = self.sleepy - 3 # Reduce score by 3
        # If score reaches 0
        if self.sleepy < 0:
            self.sleepy = 0