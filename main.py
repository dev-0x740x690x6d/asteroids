import pygame
from constants import *
from player import Player

def main():
    pygame.init()

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    player_screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    background_color = "#000000" #black

    game_clock = pygame.time.Clock()
    dt = 0

    player_x = SCREEN_WIDTH / 2
    player_y = SCREEN_HEIGHT / 2
    player = Player(player_x, player_y)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        player.update(dt)
        player_screen.fill(background_color)
        player.draw(player_screen)
        pygame.display.flip()
        dt = game_clock.tick(60) / 1000
        



if __name__ == "__main__":
    main()