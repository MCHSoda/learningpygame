import pygame
from pipboy import Pipboy
import game_functions as gf

from settings import Settings

def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("pygame")

    pipboy = Pipboy(screen)



    bg_color = (0, 0, 102)
    screen.fill(ai_settings.bg_color)
    pipboy.blitme()

    while True:
        gf.check_events()
        gf.update_screen(ai_settings, screen, pipboy)



run_game()