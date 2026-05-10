import math
import pygame
import random

class Particle():

    def __init__(self, pos=(0, 0), size=15, life=1000, color=None, shape="circ", vel=None, rainbow=True):
        self.pos = pos
        self.size = size
        self.age = 0
        self.life = life
        self.dead = False
        self.shape = shape
        self.rainbow = rainbow
        self.hue = random.randint(0, 360)
        

        if vel is None:
            self.vel = [random.uniform(-0.2, 0.2), random.uniform(1.5, 3)]
        else:
            self.vel = vel

        if color is None:
            self.color = pygame.Color(random.randrange(0, 255),
                                      random.randrange(0, 255),
                                      random.randrange(0, 255),)
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

        if self.rainbow:
            self.hue = (self.pos[1] * 0.5) % 360
            self.color = pygame.Color(0)
            self.color.hsva = (self.hue, 100, 100, 100)

    def draw(self, screen):
        surf = pygame.Surface((self.size, self.size), pygame.SRCALPHA)
        color = (self.color.r, self.color.g, self.color.b, int(self.alpha))

        pygame.draw.circle(surf, color, (self.size // 2, self.size // 2), self.size // 2)
        screen.blit(surf, self.pos)

def follow_cursor(particles, mouse_pos):

    mouse_x, mouse_y = mouse_pos

    particles.append(Particle(pos=(mouse_x + random.randint(-4, 4),
                                    mouse_y + random.randint(-4, 4)),
                                       size=random.randrange(4, 8),
                                         life=1000))


def explosion_particles(particles,mouse_pos, amount=50):

    mouse_x, mouse_y = mouse_pos

    for _ in range(amount):

                angle = random.uniform(0, math.pi * 2)
                speed = random.uniform(2, 6)
                vel_x = math.cos(angle) * speed
                vel_y = math.sin(angle) * speed

                explosion_color = pygame.Color(255,
                                               random.randint(31, 255),
                                               random.randint(25, 165))

                particles.append(Particle(pos=(mouse_x, mouse_y), 
                                          vel=[vel_x, vel_y], 
                                          size=5, 
                                          life=500,
                                          color=explosion_color,
                                          rainbow=False))
                

def cursor_shape(screen, mouse_pos):

    mouse_x, mouse_y =mouse_pos

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
    pygame.draw.polygon(screen, (242, 209, 41), transition_points,)
    pygame.draw.polygon(screen, (240, 165, 17), transition_points, 2)

def main():

    pygame.init()

    pygame.mouse.set_visible(False)

    screen = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()

    particles = []

    run = True
    while run:
        screen.fill((10, 10, 20))

        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run =False

            if event.type == pygame.MOUSEBUTTONDOWN:
                explosion_particles(particles, mouse_pos)

        follow_cursor(particles, mouse_pos)

        cursor_shape(screen, mouse_pos)

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