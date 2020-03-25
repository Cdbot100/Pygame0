import sys, pygame, random
from pygame.locals import *

pygame.init()
screen_info = pygame.display.Info()

# set the width and height to the size of the screen
size = (width, height) = (int(screen_info.current_w), int(screen_info.current_h))
screen = pygame.display.set_mode(size)

clock = pygame.time.Clock()
color = (0,127,255)

#load image and rect
fish_image = pygame.image.load("kindpng_4889542.png")
fish_image = pygame.transform.smoothscale(fish_image, (80,80))
fish_rect = fish_image.get_rect()

def main():
    while True:
        clock.tick(60)
        screen.fill(color)
        screen.blit(fish_image, fish_rect)
        pygame.display.flip()


if __name__=="__main__":
    main()

