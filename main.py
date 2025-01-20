# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *
from asteroidfield import *
from asteroids import *
from shot import *


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
    
    # instantiate Player object
    player_start_x = SCREEN_WIDTH / 2
    player_start_y = SCREEN_HEIGHT / 2
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    
    AsteroidField.containers = updateable
    Asteroid.containers = asteroids, updateable, drawable
    Player.containers = updateable, drawable
    Shot.containers = shots, updateable, drawable
    player = Player(player_start_x, player_start_y)
    field = AsteroidField()

    # game loop
    game_running = True
    counter = 0
    while game_running:
        # allows for the close button on the window to quit the program
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = False

        dt = clock.tick(60) / 1000.0  # convert milliseconds to seconds

        # update all sprites
        for thing in updateable:
            
            thing.update(dt)

        # check for collisions
        for asteroid in asteroids:
            if player.check_collision(asteroid):
                print("Game over!")
                game_running = False 
            if pygame.sprite.spritecollide(asteroid, shots, True):
                asteroid.split()
                print("Asteroid hit!")
        # clear the screen
        screen.fill("black")
       
        # draw all sprites
        for thing in drawable:
            thing.draw(screen)
        
        # refresh the screen
        pygame.display.flip()
       
    # end game loop

if __name__ == "__main__":
    main()