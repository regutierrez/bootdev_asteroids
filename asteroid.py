import pygame
from circleshape import CircleShape


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def draw(self, screen):
        pygame.draw.circle(
            surface=screen,
            color="brown",
            radius=self.radius,
            width=2,
            center=(self.x, self.y),
        )

    def update(self, dt):
        self.velocity += self.velocity * dt
