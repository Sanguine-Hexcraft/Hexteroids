# this allows us to use code from
# the open-source pygame library
# through this file
import pygame
from constants import *
from player import *


def main():
    # Initialize pygame
    pygame.init()

    # Create a clock object using pygame.time.Clock.
    clock = pygame.time.Clock()
    dt = 0
    
    # Use pygame's display.set.mode() to get a new GUI window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    # Instaniate the Player object
    player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))

    # Use an infinite while loop for the game loop.
    while True:
        # This will check if the user has closed the window and exit the game loop if they do. It will make the window's close button work.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # call the player update method move the player
        player.update(dt)
        
        # At each iteration, it should
        # Use the screen's fill method to fill the screen with a solid "black" color
        screen.fill((0,0,0,))

        # Draw the player
        player.draw(screen)

        # Use pygame's display.flip() method to refresh the screen. Be sure to call this last!
        pygame.display.flip()
        
        # Limit the Frames Per Second to 60
        # .tick() returns a value, divide that value and 
        # save it to dt or "delta time"
        dt = clock.tick(60) / 1000
    
    
if __name__ == "__main__":
    main()
