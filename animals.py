import pygame


class Animals():
    def __init__(self, screen, k, x, y, image_name, sound, x_b=0):
        """инициализация животых"""
        """k - кол-во кадров, x&y - координаты в окне, name - имя изображения, x_b - скорость движения по оси x, screen - экран"""

        pygame.mixer.init()
        self.sound = pygame.mixer.Sound(sound)

        self.screen = screen
        self.show = True
        self.k = k
        self.x_pos = x
        self.y_pos = y
        self.x_boost = x_b

        self.counter = 0
        """счетчик кадров"""

        self.animation_frames = []

        self.image = pygame.image.load(image_name).convert_alpha()

        self.width, self.height = self.image.get_size()
        self.w, self.h = self.width / k, self.height / 1

        for i in range(int(self.width / self.w)):
            # добавляем  в список отдельные кадры
            self.animation_frames.append(self.image.subsurface(pygame.Rect(i * self.w, 0, self.w, self.h)))

        self.screen_rect = screen.get_rect()

    def output(self):
        """рисование животного"""
        if self.show:
            self.x_pos += self.x_boost
            if self.x_pos >= self.screen_rect.width or self.x_pos <= -self.w:
                for i in range(len(self.animation_frames)):
                    self.animation_frames[i] = pygame.transform.flip(self.animation_frames[i], True, False)
                self.x_boost = -self.x_boost
            self.screen.blit(self.animation_frames[self.counter], (self.x_pos, self.y_pos))
            self.counter = (self.counter + 1) % self.k
