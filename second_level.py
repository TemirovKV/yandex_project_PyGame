import pygame
import sys
import random
from animals import Animals
from final_screen import stop


def run2():
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

    do_task_list(sprites)

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
                            for i2 in curr_anim.keys():
                                if curr_anim[i2] is True:
                                    if i2.image == i.image:
                                        sprites.remove(i2)
                                        del curr_anim[i2]
                                        do_task_list(sprites)
                                        i.show = False
                                        break
                                    else:
                                        break
                    else:
                        clicked_animals += 1
                if clicked_animals == len(sprites):
                    stop()

        screen.blit(bg, (0, -150))
        timer.tick(fps)
        horse.output()
        ram.output()
        cow.output()
        pigeon.output()
        pygame.display.flip()


curr_anim = dict()


def do_task_list(sprites):
    spr = sprites[:]
    random.shuffle(spr)
    for i in range(len(spr)):
        curr_anim[spr[i]] = False
    if curr_anim:
        curr_anim[spr[0]] = True
        spr[0].sound.play()
