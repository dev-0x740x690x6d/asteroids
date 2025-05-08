import pygame
from constants import *

def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    player_screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    background_color = "#000000" #black
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        player_screen.fill(background_color)
        pygame.display.flip()
        



if __name__ == "__main__":
    main()