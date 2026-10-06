import pygame
from settings import WIDTH, HEIGHT, PLAYER_SPEED, CYAN, WHITE

class Player:
    def __init__(self):
        self.rect = pygame.Rect(WIDTH // 2 - 18, HEIGHT // 2 - 18, 36, 36)
        self.speed = PLAYER_SPEED
        self.lives = 3
        self.energy = 100
        self.score = 0
        self.invulnerable = 0
        self.anim_time = 0

    def reset(self):
        self.rect.center = (WIDTH // 2, HEIGHT // 2)
        self.lives = 3
        self.energy = 100
        self.score = 0
        self.invulnerable = 0

    def update(self, keys, dt):
        dx = keys[pygame.K_d] - keys[pygame.K_a]
        dy = keys[pygame.K_s] - keys[pygame.K_w]

        if keys[pygame.K_LEFT]:
            dx -= 1
        if keys[pygame.K_RIGHT]:
            dx += 1
        if keys[pygame.K_UP]:
            dy -= 1
        if keys[pygame.K_DOWN]:
            dy += 1

        if dx or dy:
            direction = pygame.Vector2(dx, dy).normalize()
            self.rect.x += round(direction.x * self.speed)
            self.rect.y += round(direction.y * self.speed)

        self.rect.clamp_ip(pygame.Rect(30, 90, WIDTH - 60, HEIGHT - 120))
        self.anim_time += dt
        self.invulnerable = max(0, self.invulnerable - dt)

    def hit(self):
        if self.invulnerable <= 0:
            self.lives -= 1
            self.energy = max(0, self.energy - 30)
            self.invulnerable = 1.2
            self.rect.center = (WIDTH // 2, HEIGHT // 2)
            return True
        return False

    def draw(self, surface):
        if self.invulnerable > 0 and int(self.invulnerable * 12) % 2 == 0:
            return

        # Técnica: transformação de escala baseada em seno.
        pulse = 1 + 0.10 * __import__("math").sin(self.anim_time * 7)
        size = int(18 * pulse)
        center = self.rect.center

        pygame.draw.circle(surface, CYAN, center, size + 6, 2)
        pygame.draw.polygon(
            surface, CYAN,
            [(center[0], center[1] - size),
             (center[0] + size, center[1] + size),
             (center[0], center[1] + size // 2),
             (center[0] - size, center[1] + size)]
        )
        pygame.draw.circle(surface, WHITE, center, 5)
