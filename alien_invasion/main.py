import sys
import pygame
from pygame import event
from pipboy import Pipboy

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
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        pygame.display.flip()


run_game()