import pygame
import sys


def stop():
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Животинки")
    bg = pygame.image.load("data/game_bg.jpg").convert_alpha()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.blit(bg, (0, 0))
        draw_final(screen)
        pygame.display.flip()


def draw_final(screen):
    font = pygame.font.Font(None, 150)
    text = font.render("Конецъ", True, (255, 165, 0))
    text_x = 600 - text.get_width() // 2
    text_y = 400 - text.get_height() // 2
    text_w = text.get_width()
    text_h = text.get_height()
    screen.blit(text, (text_x, text_y - 70))
    pygame.draw.rect(screen, (255, 165, 0), (text_x - 10, text_y - 80,
                                             text_w + 20, text_h + 20), 1)
