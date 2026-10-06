import pygame
import random
import math

class Particle:
    def __init__(self, pos, color):
        self.pos = pygame.Vector2(pos)
        angle = random.random() * math.tau
        speed = random.uniform(40, 130)
        self.velocity = pygame.Vector2(math.cos(angle), math.sin(angle)) * speed
        self.life = random.uniform(0.3, 0.8)
        self.max_life = self.life
        self.color = color

    def update(self, dt):
        self.pos += self.velocity * dt
        self.velocity *= 0.94
        self.life -= dt

    def draw(self, surface):
        if self.life <= 0:
            return
        radius = max(1, int(4 * self.life / self.max_life))
        pygame.draw.circle(surface, self.color, (int(self.pos.x), int(self.pos.y)), radius)

class ParticleSystem:
    def __init__(self):
        self.particles = []

    def burst(self, pos, color, amount=12):
        self.particles.extend(Particle(pos, color) for _ in range(amount))

    def update(self, dt):
        for p in self.particles:
            p.update(dt)
        self.particles = [p for p in self.particles if p.life > 0]

    def draw(self, surface):
        for p in self.particles:
            p.draw(surface)
