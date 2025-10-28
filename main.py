# this allows us to use code from
# the open-source pygame library
# through this file
import pygame
from constants import *


def main():
    # Initialize pygame
    pygame.init()
    
    # Use pygame's display.set.mode() to get a new GUI window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    # Use an infinite while loop for the game loop.
    while True:
        # This will check if the user has closed the window and exit the game loop if they do. It will make the window's close button work.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # At each iteration, it should
        # Use the screen's fill method to fill the screen with a solid "black" color
        screen.fill((0,0,0,))
        # Use pygame's display.flip() method to refresh the screen. Be sure to call this last!
        pygame.display.flip()
    
if __name__ == "__main__":
    main()
