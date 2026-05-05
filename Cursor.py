import math
import pygame
import random

class Particle():

    def __init__(self, pos=(0, 0), size=15, life=1000, color=None, shape="circ"):
        self.pos = pos
        self.size = size
        self.age = 0
        self.life = life
        self.dead = False
        self.shape = shape
        self.vel = [random.uniform(-1, 1)]

        if color is None:
            self.color = pygame.Color(random.randrange(0, 255),
                                   random.randrange(0, 255),
                                    random.randrange(0, 255))
        else:
            self.color = color

        self.alpha = 255
        self.surface = self.update_surface()

    def update(self, dt):
        self.age += dt
        if self.age > self.life:
            #print("Particle is dead")
            self.dead = True

        self.vel[1] += 0.5
        self.alpha = 255 * (1 - (self.age / self.life))

    def draw(self, screen):
        surf = pygame.Surface((self.size, self.size), pygame.SRCALPHA)
        color = (*self.color[:3], int(self.alpha))

        pygame.draw.circle(surf, color, (self.color // 2, self.color // 2), self.color // 2)
        screen.blit(surf, self.pos)


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