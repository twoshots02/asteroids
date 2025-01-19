import pygame
from constants import *

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(self.containers)
        self.position = pygame.Vector2(x, y)
        self.rotation = 0
        self.radius = 20  # Example radius, adjust as needed

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)
    
    def rotate(self, direction, dt):
        self.rotation += PLAYER_TURN_SPEED * dt * direction
        self.rotation %= 360
    
    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-1, dt)
        if keys[pygame.K_d]:
            self.rotate(1, dt)
        if keys[pygame.K_w]:
            self.move(1, dt)
        if keys[pygame.K_s]:
            self.move(-1, dt)

    def move(self, direction, dt):
        
        self.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SPEED
        
        self.position += self.velocity * dt * direction