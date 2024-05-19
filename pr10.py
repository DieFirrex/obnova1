import pygame
import pygame_menu
import os
from starwars import *
pygame.init()

window = pygame.display.set_mode((500, 500))

font1 = pygame_menu.font.FONT_MUNRO
my_theme = pygame_menu.Theme(widget_font=font1,
                             background_color=(0, 0, 0),
                             widget_font_color=(255, 0, 0))

def start():
    game_1111()
#----------------------------------------------------------------
menu_rules = pygame_menu.Menu("Rules",500,500,
                        theme=my_theme)
menu_rules.add.label("Game Rules :\n1.Don't lose!\n")
#----------------------------------------------------------------
menu_settings = pygame_menu.Menu("Settings",500,500,
                                 theme=my_theme)
menu_settings.add.label("Settings\n")
menu_settings.add.selector("Difficulty:\n",[('Easy',1),('Hard',2)])
#----------------------------------------------------------------
menu = pygame_menu.Menu("Main Menu",500,500,
                        theme=my_theme)
menu.add.button("Start",start)
menu.add.button("Settings",menu_settings)
menu.add.button("Rulles",menu_rules)
menu.add.button("Exit",pygame_menu.events.EXIT)
#----------------------------------------------------------------
menu.mainloop(window)

