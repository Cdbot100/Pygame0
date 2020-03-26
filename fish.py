import pygame, random

class Fish:
    def __init__(self,pos):
        # load image and rect
        self.image = pygame.image.load("kindpng_4889542.png")
        self.image = pygame.transform.smoothscale(self.image, (80, 80))
        self.rect = self.image.get_rect()
        self.rect.center = pos

        # Set speed and rotation
        self.speed = pygame.math.Vector2(0, 10)
        rotation = random.randint(0, 360)
        self.speed.rotate_ip(rotation)
        self.image = pygame.transform.rotate(self.image, 180 - rotation)

    def update(self):
        screen_info = pygame.display.Info()
        self.rect.move_ip(self.speed)
        if self.rect.left < 0 or self.rect.right > screen_info.current_w:
            self.speed[0] *= -1
            self.image = pygame.transform.flip(self.image, True, False)
            self.rect.move_ip(self.speed[0], 0)
        if self.rect.top < 0 or self.rect.bottom > screen_info.current_h:
            self.speed[1] *= -1
            self.image = pygame.transform.flip(self.image, True, False)
            self.rect.move_ip(self.speed[1], 0)

    def draw(self, screen):
        screen.blit(self.image,self.rect)