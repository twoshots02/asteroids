from constants import *
import pygame
import random
from circleshape import CircleShape
from player import Player

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.image = pygame.Surface((self.radius * 2, self.radius * 2))
        self.image.set_colorkey("black")
        self.rect = self.image.get_rect()
        self.rect.center = (self.position.x, self.position.y)
        self.rotation = 0
        self.rotation_speed = random.uniform(-ASTEROID_ROTATION_SPEED, ASTEROID_ROTATION_SPEED)
        self.velocity = pygame.Vector2(0, 0)

    def update(self, dt):
        self.position += self.velocity * dt
        self.rotation += self.rotation_speed * dt
        self.rotation %= 360
        self.rect.center = (self.position.x, self.position.y)

    def draw(self, screen):
        pygame.draw.circle(screen, "gray", (int(self.position.x), int(self.position.y)), self.radius)
        pygame.draw.circle(screen, "black", (int(self.position.x), int(self.position.y)), self.radius, 2)

    def check_collision(self, other):
        if isinstance(other, Player):
            if self.position.distance_to(other.position) < self.radius + other.radius:
                return True
        return False
    
    def split(self):
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()
            return
        for _ in range(2):
            asteroid = Asteroid(self.position.x, self.position.y, self.radius // 2)
            asteroid.velocity = self.velocity.rotate(random.randint(-40, 40))
            asteroid.rotation_speed = random.uniform(-ASTEROID_ROTATION_SPEED, ASTEROID_ROTATION_SPEED)
            asteroid.image = pygame.Surface((asteroid.radius * 2, asteroid.radius * 2))
            asteroid.image.set_colorkey("black")
            asteroid.rect = asteroid.image.get_rect()
            asteroid.rect.center = (asteroid.position.x, asteroid.position.y)

        self.kill()



