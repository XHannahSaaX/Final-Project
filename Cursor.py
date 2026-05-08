import math
import pygame
import random

class Particle():

    def __init__(self, pos=(0, 0), size=15, life=1000, color=None, shape="circ", vel=None):
        self.pos = pos
        self.size = size
        self.age = 0
        self.life = life
        self.dead = False
        self.shape = shape
        

        if vel is None:
            self.vel = [random.uniform(-0.2, 0.2), random.uniform(1.5, 3)]
        else:
            self.vel = vel

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

        self.vel[1] += 0.005
        self.pos = (self.pos[0] + self.vel[0] * dt * 0.05,
                     self.pos[1] + self.vel[1] * dt * 0.05)
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

        for _ in range(1):
            particles.append(Particle(pos=(mouse_x + random.randint(-4, 4),
                                            mouse_y + random.randint(-4, 4)),
                                       size=random.randrange(4, 8),
                                         life=1000))
            
        star_points = [
            (0, -10),
            (3, -3),
            (10, -3),
            (4, 2),
            (6, 9),
            (0, 5),
            (-6, 9),
            (-4, 2),
            (-10, -3),
            (-3, -3)
        ]

        transition_points = [(x + mouse_x, y + mouse_y) for x, y in star_points]
        pygame.draw.polygon(screen, (190, 16, 224), transition_points, 3)

        if event.type == pygame.MOUSEBUTTONDOWN:
            for _ in range(50):

                angle = random.uniform(0, math.pi * 2)
                speed = random.uniform(2, 8)
                vel_x = math.cos(angle) * speed
                vel_y = math.sin(angle) * speed

                particles.append(Particle(pos=(mouse_x, mouse_y), vel=[vel_x, vel_y], size=5, life=1000))

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