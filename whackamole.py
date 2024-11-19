import pygame, sys
import random

game_over = False
grid_size = 32

light_blue = "#c2d9ff"

def main():
    try:
        pygame.init()
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True

        mole_x = random.randrange(0, 512, grid_size)
        mole_y = random.randrange(0, 640, grid_size)

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x,y = event.pos
                    row = y // grid_size
                    col = x // grid_size

                    mole_row = mole_y // grid_size
                    mole_col = mole_x // grid_size

                    if (row, col) == (mole_row, mole_col):
                        mole_x = random.randrange(0, 640, grid_size)
                        mole_y = random.randrange(0, 512, grid_size)

            screen.fill(light_blue)
            display_grid(screen)
            screen.blit(mole_image, mole_image.get_rect(topleft=(mole_x, mole_y)))
            pygame.display.flip()
            clock.tick(60)

    finally:
        pygame.quit()

def display_grid(screen):

    for x in range(0, 640, grid_size):
        pygame.draw.line(screen, "black", (x, 0), (x, 512))

    for y in range(0, 512, grid_size):
        pygame.draw.line(screen, "black", (0,y), (640,y))

if __name__ == "__main__":
    main()
