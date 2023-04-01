import os
import pygame
import pygame_menu

pygame.init()
surface = pygame.display.set_mode((600, 400))



def start_the_game():
    
    os.system("python game.py")

menu = pygame_menu.Menu('Welcome', 400, 300,
                       theme=pygame_menu.themes.THEME_BLUE)

menu.add.text_input('Name :', default='Call the Police')
menu.add.button('Play', start_the_game)
menu.add.button('Quit', pygame_menu.events.EXIT)
menu.mainloop(surface)

