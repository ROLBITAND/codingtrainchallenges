import pygame
from random import randint
from collections import namedtuple

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

Point = namedtuple("Point", ["x", "y"])

ORIGIN = Point(x=SCREEN_WIDTH // 2, y=SCREEN_HEIGHT // 2)

class Star:
    def __init__(self):
        self.reset()

    def update(self):
        self.z -= 10
        if self.z <= 0:
            self.reset()

    def draw(self, surf):
        sx = (self.x / self.z) * (SCREEN_WIDTH // 2)
        sy = (self.y / self.z) * (SCREEN_HEIGHT // 2)
        pygame.draw.circle(
            surf,
            "white",
            (ORIGIN.x - sx, ORIGIN.y - sy),
            pygame.math.remap(2000, 1, 1, 4, self.z),
        )

    def reset(self):
        self.x = randint(-SCREEN_WIDTH // 2, SCREEN_WIDTH // 2)
        self.y = randint(-SCREEN_HEIGHT, SCREEN_HEIGHT)
        self.z = randint(1, 2000)


def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    surf = pygame.Surface((SCREEN_WIDTH * 2, SCREEN_HEIGHT * 2), pygame.SRCALPHA)
    clock = pygame.time.Clock()
    running = True

    # setup
    stars = [Star() for _ in range(200)]

    # update
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill("black")
        surf.fill(0)

        for star in stars:
            star.update()
            star.draw(surf)

        screen.blit(surf, (0, 0))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()