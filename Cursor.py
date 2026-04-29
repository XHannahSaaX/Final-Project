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

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run =False

        mouse_x, mouse_y = pygame.mouse.get_pos()

        pygame.draw.circle(screen, (190, 16, 224), (mouse_x, mouse_y), 10)

        pygame.display.flip()


        clock.tick(60)

pygame.quit()

if __name__ == "__main__":
    main()