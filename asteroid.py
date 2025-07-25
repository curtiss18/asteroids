import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", (int(self.position.x), int(self.position.y)), self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        split_angle = random.uniform(20, 50)
        asteroid_1_velocity = self.velocity.rotate(split_angle)
        asteroid_2_velocity = self.velocity.rotate(-split_angle)
        new_asteroids_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid_1 = Asteroid(self.position.x, self.position.y, new_asteroids_radius)
        asteroid_1.velocity = asteroid_1_velocity * 1.2
        asteroid_2 = Asteroid(self.position.x, self.position.y, new_asteroids_radius)
        asteroid_2.velocity = asteroid_2_velocity * 1.2

        