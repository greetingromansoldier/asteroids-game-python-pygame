import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__ (self, x, y, radius):
        super().__init__(x, y, radius)

    def draw (self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update (self, dt):
        self.position += self.velocity * dt

    def split (self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            angle = random.uniform(20, 25)
            random_angle1 = self.velocity.rotate(angle)
            random_angle2 = self.velocity.rotate(-angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            new_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid1.velocity = random_angle1
            new_asteroid1.velocity *= 1.2
            new_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid2.velocity = random_angle2
            new_asteroid2.velocity *= 1.2
