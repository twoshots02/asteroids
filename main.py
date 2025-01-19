# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *

def main():
    game_running = True
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
# set screen resolution
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# set clock limiter for FPS limiting
    clock = pygame.time.Clock()
    dt = 0

# game loop
    while game_running:
        #allows for the close button on the window to quit the program
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return        

        dt = clock.tick(60)

if __name__ == "__main__":
    main()    