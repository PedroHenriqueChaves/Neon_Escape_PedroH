import pygame
import random
import math
from settings import WIDTH, HEIGHT, RED, MAGENTA

class Enemy:
    def __init__(self, difficulty=1):
        side = random.choice(["top", "bottom", "left", "right"])
        if side == "top":
            x, y = random.randint(50, WIDTH-50), 100
        elif side == "bottom":
            x, y = random.randint(50, WIDTH-50), HEIGHT-80
        elif side == "left":
            x, y = 50, random.randint(110, HEIGHT-60)
        else:
            x, y = WIDTH-50, random.randint(110, HEIGHT-60)

        self.rect = pygame.Rect(x-15, y-15, 30, 30)
        self.speed = 1.4 + difficulty * 0.18 + random.random() * 0.7
        self.phase = random.random() * math.tau
        self.anim = 0

    def update(self, target, dt):
        self.anim += dt
        direction = pygame.Vector2(target.rect.center) - pygame.Vector2(self.rect.center)
        if direction.length_squared():
            direction = direction.normalize()

        # Pequena oscilação para evitar movimento totalmente linear.
        wave = pygame.Vector2(
            math.cos(self.anim * 3 + self.phase),
            math.sin(self.anim * 3 + self.phase)
        ) * 0.35

        velocity = direction * self.speed + wave
        self.rect.x += round(velocity.x)
        self.rect.y += round(velocity.y)

    def draw(self, surface):
        pygame.draw.circle(surface, MAGENTA, self.rect.center, 19, 2)
        pygame.draw.rect(surface, RED, self.rect, border_radius=7)
        pygame.draw.line(surface, (255, 180, 210),
                         (self.rect.left+7, self.rect.top+7),
                         (self.rect.right-7, self.rect.bottom-7), 2)
        pygame.draw.line(surface, (255, 180, 210),
                         (self.rect.right-7, self.rect.top+7),
                         (self.rect.left+7, self.rect.bottom-7), 2)
