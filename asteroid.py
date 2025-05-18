import pygame
import random
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "#ffffff", self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()
            return
        current_position = pygame.Vector2(self.position)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        new_angle = random.uniform(20, 50)
        asteroid_1 = Asteroid(current_position.x, current_position.y, new_radius)
        asteroid_2 = Asteroid(current_position.x, current_position.y, new_radius)
        asteroid_1.velocity = self.velocity.rotate(new_angle) * 1.2
        asteroid_2.velocity = self.velocity.rotate(-new_angle) * 1.2
        self.kill()
        