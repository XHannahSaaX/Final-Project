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
        self.vel = [random.uniform(-1, 1), random.uniform(1, 3)]

        if color is None:
            self.color = pygame.Color(random.randrange(0, 255),
                                   random.randrange(0, 255),
                                    random.randrange(0, 255))
        else:
            self.color = color

        self.alpha = 255

    def update(self, dt):
        self.age += dt
        if self.age > self.life:
            self.dead = True

        self.vel[1] += 0.5
        self.alpha = max(0, 255 * (1 - (self.age / self.life)))

    def draw(self, screen):
        surf = pygame.Surface((self.size, self.size), pygame.SRCALPHA)
        color = (self.color.r, self.color.g, self.color.b, int(self.alpha))

        pygame.draw.circle(surf, color, (self.size // 2, self.size // 2), self.size // 2)
        screen.blit(surf, self.pos)


def main():

    pygame.init()

    pygame.mouse.set_visible(False)

    screen = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()

    particles = []

    run = True
    while run:
        screen.fill((10, 10, 20))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run =False

        mouse_x, mouse_y = pygame.mouse.get_pos()

        for _ in range(5):
            particles.append(Particle(pos=(mouse_x, mouse_y), size=random.randrange(5, 10), life=500))

        pygame.draw.circle(screen, (190, 16, 224), (mouse_x, mouse_y), 5)

        dt = clock.get_time()

        for p in particles[:]:
            p.update(dt)
            p.draw(screen)

            if p.dead:
                particles.remove(p)


        pygame.display.flip()


        clock.tick(60)

pygame.quit()

if __name__ == "__main__":
    main()