import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    background_color = "#000000" #black

    game_clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)

    player_x = SCREEN_WIDTH / 2
    player_y = SCREEN_HEIGHT / 2
    player = Player(player_x, player_y)

    player.timer 

    asteroid_field = AsteroidField()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(background_color)
        
        for draw_object in drawable:
            draw_object.draw(screen)

        for update_object in updatable:
            update_object.update(dt)

        for ast_obj in asteroids:
            if ast_obj.is_colliding(player) == True:
                print("GAME OVER!")
                sys.exit()

        for ast_obj in asteroids:
            for shot_obj in shots:
                if shot_obj.is_colliding(ast_obj) == True:
                    ast_obj.split()
                    shot_obj.kill()

        pygame.display.flip()
        dt = game_clock.tick(60) / 1000
        
if __name__ == "__main__":
    main()