import pygame


SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720


def draw_square(surf, x, y, size, level=0):
    # base case
    if level == 0:
        rect = pygame.Rect(0, 0, size, size)
        rect.center = x, y
        pygame.draw.rect(surf, "white", rect)
    else:
        divided_size = size // 3

        # create an 3x3 square grid where the middle is missing
        for square_ninth in [(-1, -1), (0, -1), (1, -1),
                           (-1, 0),           (1, 0),
                           (-1, 1),  (0, 1),  (1, 1)]:
            draw_square(
                surf,
                # the square_ninth vectors move the original coords 
                x + (square_ninth[0] * divided_size),
                y + (square_ninth[1] * divided_size),
                divided_size,
                level - 1,
            )


def main():
    pygame.init()
    window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    running = True
    recursion_level = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                # Q - decrease recursion level
                if event.key == pygame.K_LEFT:
                    recursion_level = max(0, recursion_level - 1)
                # E - increase recursion level
                if event.key == pygame.K_RIGHT:
                    recursion_level += 1

        window.fill("black")

        draw_square(window, SCREEN_WIDTH//2, SCREEN_HEIGHT//2, 600, recursion_level)
        
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()