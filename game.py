import pygame
import random
from settings import *
from player import Player
from enemy import Enemy
from collectible import Collectible
from particles import ParticleSystem
from ui import UI

class Game:
    MENU = "menu"
    INSTRUCTIONS = "instructions"
    PLAYING = "playing"
    PAUSED = "paused"
    GAME_OVER = "game_over"
    VICTORY = "victory"

    def __init__(self):
        self.state = self.MENU
        self.player = Player()
        self.ui = UI()
        self.particles = ParticleSystem()
        self.enemies = []
        self.collectibles = []
        self.level = 1
        self.elapsed = 0
        self.spawn_timer = 0
        self.collect_timer = 0

    def start(self):
        self.player.reset()
        self.level = 1
        self.enemies = [Enemy(self.level) for _ in range(INITIAL_ENEMIES)]
        self.collectibles = [Collectible() for _ in range(4)]
        self.elapsed = 0
        self.spawn_timer = 0
        self.collect_timer = 0
        self.state = self.PLAYING

    def handle_event(self, event):
        if event.type != pygame.KEYDOWN:
            return

        if self.state == self.MENU:
            if event.key == pygame.K_RETURN:
                self.start()
            elif event.key == pygame.K_i:
                self.state = self.INSTRUCTIONS
            elif event.key == pygame.K_ESCAPE:
                pygame.quit()
                raise SystemExit

        elif self.state == self.INSTRUCTIONS:
            if event.key == pygame.K_ESCAPE:
                self.state = self.MENU
            elif event.key == pygame.K_RETURN:
                self.start()

        elif self.state == self.PLAYING:
            if event.key == pygame.K_ESCAPE:
                self.state = self.PAUSED

        elif self.state == self.PAUSED:
            if event.key == pygame.K_ESCAPE:
                self.state = self.PLAYING
            elif event.key == pygame.K_m:
                self.state = self.MENU

        elif self.state in (self.GAME_OVER, self.VICTORY):
            if event.key == pygame.K_RETURN:
                self.start()
            elif event.key == pygame.K_ESCAPE:
                self.state = self.MENU

    def update(self, dt):
        if self.state != self.PLAYING:
            return

        self.elapsed += dt
        keys = pygame.key.get_pressed()
        self.player.update(keys, dt)

        # Progressão: nova fase a cada 15 segundos.
        new_level = min(8, 1 + int(self.elapsed // 15))
        if new_level != self.level:
            self.level = new_level
            self.particles.burst(self.player.rect.center, YELLOW, 24)

        for enemy in self.enemies:
            enemy.update(self.player, dt)
            if enemy.rect.colliderect(self.player.rect):
                if self.player.hit():
                    self.particles.burst(self.player.rect.center, MAGENTA, 18)

        for item in self.collectibles:
            item.update(dt)
            if item.rect.colliderect(self.player.rect):
                if item.kind == "energy":
                    self.player.energy = min(100, self.player.energy + 20)
                    self.player.score += 100
                    color = GREEN
                else:
                    self.player.score += 250
                    color = YELLOW
                self.particles.burst(item.rect.center, color, 16)
                item.rect.center = (
                    random.randint(70, WIDTH-70),
                    random.randint(120, HEIGHT-70)
                )

        self.spawn_timer += dt
        spawn_interval = max(1.0, 4.0 - self.level * 0.3)
        if self.spawn_timer >= spawn_interval and len(self.enemies) < min(MAX_ENEMIES, 3+self.level):
            self.spawn_timer = 0
            self.enemies.append(Enemy(self.level))

        self.collect_timer += dt
        if self.collect_timer >= 7:
            self.collect_timer = 0
            self.collectibles.append(Collectible())
            self.collectibles = self.collectibles[-7:]

        # Vitória por pontuação ou sobrevivência de 60 s.
        if self.player.score >= GOAL_SCORE or self.elapsed >= ROUND_TIME:
            self.state = self.VICTORY

        if self.player.lives <= 0 or self.player.energy <= 0:
            self.state = self.GAME_OVER

        self.particles.update(dt)

    def draw_background(self, surface):
        surface.fill(BG)

        # Técnica: composição por camadas + paralaxe simples.
        offset = int(self.elapsed * (8 + self.level * 2)) % 60
        for x in range(-60, WIDTH+60, 60):
            pygame.draw.line(surface, GRID, (x-offset, 90), (x-offset, HEIGHT), 1)
        for y in range(110, HEIGHT, 45):
            pygame.draw.line(surface, GRID, (0, y), (WIDTH, y), 1)

        # Prédios em duas camadas.
        for i in range(-1, 14):
            x = i * 85 - (offset // 2)
            h = 80 + (i % 4) * 30
            pygame.draw.rect(surface, (12, 19, 42), (x, 80, 70, h))
            for wy in range(95, 80+h-10, 18):
                pygame.draw.rect(surface, (25, 100, 120), (x+10, wy, 7, 5))

        pygame.draw.rect(surface, (9, 14, 31), (30, 90, WIDTH-60, HEIGHT-120), 2)

    def draw(self, surface):
        self.draw_background(surface)

        if self.state == self.MENU:
            self.ui.menu(surface, self.elapsed)
            return

        if self.state == self.INSTRUCTIONS:
            self.ui.instructions(surface)
            return

        for item in self.collectibles:
            item.draw(surface)
        for enemy in self.enemies:
            enemy.draw(surface)

        self.player.draw(surface)
        self.particles.draw(surface)
        self.ui.hud(surface, self.player, self.level, ROUND_TIME-self.elapsed)

        if self.state == self.PAUSED:
            self.ui.centered_message(surface, "PAUSADO", "ESC — continuar | M — menu", CYAN)
        elif self.state == self.GAME_OVER:
            self.ui.centered_message(surface, "GAME OVER", f"Pontuação: {self.player.score}", RED)
        elif self.state == self.VICTORY:
            self.ui.centered_message(surface, "VITÓRIA!", f"Pontuação: {self.player.score}", GREEN)
