import random

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, SCREEN_WIDTH, SCREEN_HEIGHT, LINE_WIDTH
import pygame

from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        # Update the asteroid's position based on its velocity and the time delta
        self.position += self.velocity * dt

    def split(self) -> list["Asteroid"]:
        # Split the asteroid into smaller asteroids if its radius is greater than the minimum
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()
            return
        else: 
            log_event("asteroid_split")
            self.kill()
            angle = random.uniform(20, 50)
            asteroid1_rotate = self.velocity.rotate(angle)
            asteroid2_rotate = self.velocity.rotate(-angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid1.velocity = asteroid1_rotate
            asteroid2.velocity = asteroid2_rotate
            return [asteroid1, asteroid2]
