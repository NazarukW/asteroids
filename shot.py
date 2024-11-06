from circleshape import CircleShape
import pygame

class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.velocity = 0

    def draw(self, screen):
        pygame.draw.circle(screen, "green", self.position, self.radius)

    def update(self, dt):
        self.position += (self.velocity * dt)
