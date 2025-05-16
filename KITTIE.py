import pygame, sys

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((1280, 720))
bg = pygame.image.load('imagez/background/kittiemainbg.png') # default background

class Button(): # baraltech YT tutorial :)
    def __init__(self, image, pos, textinput, font, colour, hovcolour):
        self.image = image
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.font = font # text font
        self.colour, self.hovcolour = colour, hovcolour # default / hover button colour
        self.textinput = textinput # text in button
        self.text = self.font.render(self.textinput, True, self.colour)
        if self.image is None:
            self.image = self.text
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

    def update(self, screen):
        if self.image is not None:
            screen.blit(self.image, self.rect)
        screen.blit(self.text, self.text_rect)

    def checkforinput(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            return True
        return False

    def changecolour(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            self.text = self.font.render(self.textinput, True, self.hovcolour)
        else:
            self.text = self.font.render(self.textinput, True, self.colour)

def getfont(size): # resizes font
    return pygame.font.Font('files/textfont.ttf', size) # apple font ttf file

def play(): # game
    pygame.display.set_caption('KITTIE: MENU')  # sets menu caption

    # Load and play music ONCE
    # pygame.mixer.music.load() (to play music)
    # pygame.mixer.music.play(-1)  # loops music

    while True: # game loop
        screen.blit(bg, (0, 0))  # sets background
        menu_mouse_pos = pygame.mouse.get_pos()

        playbutton = Button(image=pygame.image.load('imagez/buttons/optionbutton.png'), pos=(210, 650),
                            textinput='feed', font=getfont(75), colour='#91cbf2', hovcolour='#57bbff')
        optionbutton = Button(image=pygame.image.load('imagez/buttons/optionbutton.png'), pos=(640, 650),
                              textinput='sleep', font=getfont(75), colour='#91cbf2', hovcolour='#57bbff')
        quitbutton = Button(image=pygame.image.load('imagez/buttons/optionbutton.png'), pos=(1070, 650),
                            textinput='play', font=getfont(75), colour='#91cbf2', hovcolour='#57bbff')

        for button in [playbutton, optionbutton, quitbutton]:
            button.changecolour(menu_mouse_pos)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.mixer.music.stop()
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if playbutton.checkforinput(menu_mouse_pos):
                    pygame.mixer.music.stop()
                    play()
                if optionbutton.checkforinput(menu_mouse_pos):
                    options()
                if quitbutton.checkforinput(menu_mouse_pos):
                    pygame.mixer.music.stop()
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


def menu():  # menu screen
    pygame.display.set_caption('KITTIE: MENU')  # sets menu caption

    # Load and play music ONCE
    pygame.mixer.music.load('mus/kittietheme.mp3')
    pygame.mixer.music.play(-1)  # -1 loops forever

    while True:
        screen.blit(bg, (0, 0))  # sets background
        menu_mouse_pos = pygame.mouse.get_pos()

        playbutton = Button(image=pygame.image.load('imagez/buttons/optionbutton.png'), pos=(885, 350),
                            textinput='play', font=getfont(75), colour='#91cbf2', hovcolour='#57bbff')
        optionbutton = Button(image=pygame.image.load('imagez/buttons/optionbutton.png'), pos=(885, 500),
                              textinput='options', font=getfont(75), colour='#91cbf2', hovcolour='#57bbff')
        quitbutton = Button(image=pygame.image.load('imagez/buttons/optionbutton.png'), pos=(885, 650),
                            textinput='quit', font=getfont(75), colour='#91cbf2', hovcolour='#57bbff')

        for button in [playbutton, optionbutton, quitbutton]:
            button.changecolour(menu_mouse_pos)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.mixer.music.stop()
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if playbutton.checkforinput(menu_mouse_pos):
                    pygame.mixer.music.stop()
                    play()
                if optionbutton.checkforinput(menu_mouse_pos):
                    options()
                if quitbutton.checkforinput(menu_mouse_pos):
                    pygame.mixer.music.stop()
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

menu()
