import pygame, sys
from buttonfunc import Button
from kittieclass import Kittie

pygame.init()
pygame.mixer.init()

# size of display
screen = pygame.display.set_mode((1280, 720))

# font sizing
def getfont(size):
    return pygame.font.Font('files/textfont.ttf', size) # apple font ttf file

# game
def start():
    pygame.display.set_caption('KITTIE: MENU')  # sets menu caption
    bg = pygame.image.load('imagez/background/bgblockcol.png') # sets background

    # Load and play music ONCE
    # pygame.mixer.music.load() (to play music)
    # pygame.mixer.music.play(-1)  # loops music

    while True: # game loop
        screen.blit(bg, (0, 0))  # sets background
        menu_mouse_pos = pygame.mouse.get_pos()

        feedbutton = Button(image=pygame.image.load('imagez/buttons/optionbutton.png'), pos=(210, 650),
                            textinput='feed', font=getfont(75), colour='#91cbf2', hovcolour='#57bbff')
        sleepbutton = Button(image=pygame.image.load('imagez/buttons/optionbutton.png'), pos=(640, 650),
                              textinput='sleep', font=getfont(75), colour='#91cbf2', hovcolour='#57bbff')
        playbutton = Button(image=pygame.image.load('imagez/buttons/optionbutton.png'), pos=(1070, 650),
                            textinput='play', font=getfont(75), colour='#91cbf2', hovcolour='#57bbff')
        exitbutton = Button(image=pygame.image.load('imagez/buttons/optionbutton.png'), pos=(1070, 130),
                            textinput='exit', font=getfont(75), colour='#91cbf2', hovcolour='#57bbff')

        for button in [playbutton, feedbutton, sleepbutton, exitbutton]:
            button.changecolour(menu_mouse_pos)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.mixer.music.stop()
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if feedbutton.checkforinput(menu_mouse_pos):
                    pygame.mixer.music.stop()
                    # feed
                if sleepbutton.checkforinput(menu_mouse_pos):
                    pygame.mixer.music.stop()
                    # sleep
                if playbutton.checkforinput(menu_mouse_pos):
                    pygame.mixer.music.stop()
                    # play
                if exitbutton.checkforinput(menu_mouse_pos):
                    pygame.mixer.music.stop()
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

# menu screen
def main():
    pygame.display.set_caption('KITTIE: MENU')  # sets menu caption
    bg = pygame.image.load('imagez/background/kittiemainbg.png') # sets background

    # Load and play music ONCE
    pygame.mixer.music.load('mus/kittietheme.mp3')
    pygame.mixer.music.play(-1)  # -1 loops forever

    while True: # game loop
        screen.blit(bg, (0, 0))  # sets background
        menu_mouse_pos = pygame.mouse.get_pos()

    # button properties
        startbutton = Button(image=pygame.image.load('imagez/buttons/startbutton.png'), pos=(885, 350),
                            textinput='start', font=getfont(75), colour='#91cbf2', hovcolour='#57bbff')
        optionbutton = Button(image=pygame.image.load('imagez/buttons/optionbutton.png'), pos=(885, 500),
                              textinput='options', font=getfont(75), colour='#91cbf2', hovcolour='#57bbff')
        quitbutton = Button(image=pygame.image.load('imagez/buttons/quitbutton.png'), pos=(885, 650),
                            textinput='quit', font=getfont(75), colour='#91cbf2', hovcolour='#57bbff')

    # change colour of button on hover
        for button in [startbutton, optionbutton, quitbutton]:
            button.changecolour(menu_mouse_pos)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.mixer.music.stop()
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if startbutton.checkforinput(menu_mouse_pos):
                    pygame.mixer.music.stop()
                    start()
                if optionbutton.checkforinput(menu_mouse_pos):
                    # options()
                    return # change once options page defined
                if quitbutton.checkforinput(menu_mouse_pos):
                    pygame.mixer.music.stop()
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main()
