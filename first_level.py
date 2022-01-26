import pygame
import sys
from animals import Animals
from second_level import run2


def run():
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Животинки")
    bg = pygame.image.load("data/game_bg.jpg").convert_alpha()

    sprites = list()
    horse = Animals(screen, 4, 800, 400, "data/horse1.png", "data/horse.wav")
    ram = Animals(screen, 4, 400, 200, "data/ram_eat.png", "data/ram.wav")
    cow = Animals(screen, 4, 1, 300, "data/cow_walk1.png", "data/cow.wav", 8)
    pigeon = Animals(screen, 3, 300, 100, "data/pigeon.png", "data/pigeon.wav", 15)
    sprites.append(horse)
    sprites.append(ram)
    sprites.append(cow)
    sprites.append(pigeon)

    timer = pygame.time.Clock()
    fps = 8

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                clicked_animals = 0
                for i in sprites:
                    x, y, w, h = i.x_pos, i.y_pos, i.w, i.h
                    if i.show:
                        if pos[0] >= x and pos[1] >= y and pos[0] <= x + w and pos[1] <= y + h:
                            i.sound.play()
                            i.show = False
                    else:
                        clicked_animals += 1
                if clicked_animals == len(sprites):
                    run2()

        screen.blit(bg, (0, -150))
        timer.tick(fps)
        horse.output()
        ram.output()
        cow.output()
        pigeon.output()
        pygame.display.flip()
