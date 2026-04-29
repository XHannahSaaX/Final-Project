import math
import pygame
import random


def main():

    pygame.init()

    pygame.mouse.set_visible(False)

    screen = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()

    run = True
    while run:
        screen.fill((10, 10, 20))


        clock.tick(60)

pygame.quit()

if __name__ == "__main__":
    main()