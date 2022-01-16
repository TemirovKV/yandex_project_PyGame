import pygame
import sys
from main import run


def start():
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Животинки")
    bg = pygame.image.load("data/game_bg.jpg").convert_alpha()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                if pos[0] >= 486 and pos[1] >= 365 and pos[0] <= 715 and pos[1] <= 435:
                    run()
        screen.blit(bg, (0, 0))
        draw(screen)
        draw_button(screen)
        pygame.display.flip()


def draw(screen):
    font = pygame.font.Font(None, 150)
    text = font.render("Животинки", True, (255, 165, 0))
    text_x = 600 - text.get_width() // 2
    text_y = 400 - text.get_height() // 2
    screen.blit(text, (text_x, text_y - 250))


def draw_button(screen):
    font = pygame.font.Font(None, 100)
    text = font.render("Хъаз", True, (255, 165, 0))
    text_x = 600 - text.get_width() // 2
    text_y = 400 - text.get_height() // 2
    # print(text_x, text_y)
    # print(text.get_width(), text.get_height())
    text_w = text.get_width()
    text_h = text.get_height()
    screen.blit(text, (text_x, text_y))
    pygame.draw.rect(screen, (255, 165, 0), (text_x - 10, text_y - 10,
                                             text_w + 20, text_h + 20), 1)


start()
