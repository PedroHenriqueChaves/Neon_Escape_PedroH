import pygame
import random
from settings import WIDTH, HEIGHT, YELLOW, GREEN

class Collectible:
    def __init__(self, kind=None):
        self.kind = kind or random.choice(["energy", "energy", "bonus"])
        self.rect = pygame.Rect(
            random.randint(70, WIDTH-70),
            random.randint(120, HEIGHT-70),
            22, 22
        )
        self.timer = 0

    def update(self, dt):
        self.timer += dt

    def draw(self, surface):
        offset = int(3 * __import__("math").sin(self.timer * 5))
        r = self.rect.move(0, offset)
        color = GREEN if self.kind == "energy" else YELLOW
        pygame.draw.circle(surface, color, r.center, 12, 2)
        pygame.draw.circle(surface, color, r.center, 5)
