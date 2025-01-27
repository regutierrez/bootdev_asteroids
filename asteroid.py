import pygame
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS
import random


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(
            surface=screen,
            color="white",
            center=self.position,
            radius=self.radius,
            width=2,
        )

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        angle_of_split = random.uniform(20, 50)
        a = self.velocity.rotate(angle_of_split)
        b = self.velocity.rotate(-angle_of_split)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid_a = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_a.velocity = a * 1.2
        asteroid_b = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_b.velocity = b * 1.2
