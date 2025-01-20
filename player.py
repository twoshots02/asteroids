import pygame
from constants import *
from circleshape import CircleShape
from shot import Shot

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(self.containers)
        self.position = pygame.Vector2(x, y)
        self.rotation = 0
        self.radius = 20  # Example radius, adjust as needed
        self.cooldown = 0

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
        if keys[pygame.K_SPACE]:
            self.shoot()
        if self.cooldown > 0: self.cooldown -= dt
        

    def move(self, direction, dt):
        
        self.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SPEED
        
        self.position += self.velocity * dt * direction
 
    def check_collision(self, other):
        
        if self.position.distance_to(other.position) < self.radius + other.radius:
            return True
        return False
    
    def shoot(self):
        if self.cooldown > 0:
            return None
        self.shot = Shot(self.position.x, self.position.y, SHOT_RADIUS)
        self.shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        self.cooldown = PLAYER_SHOOT_COOLDOWN
        return self.shot
        