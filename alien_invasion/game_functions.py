import pygame

import sys


def check_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


def update_screen(ai_settings, screen, pipboy):
    screen.fill(ai_settings.bg_color)
    pipboy.blitme()

    pygame.display.flip()
