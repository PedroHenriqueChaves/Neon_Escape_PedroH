import pygame
from settings import WIDTH, CYAN, MAGENTA, WHITE, GRAY, DARK, GREEN, YELLOW, RED

class UI:
    def __init__(self):
        self.big = pygame.font.Font(None, 64)
        self.title = pygame.font.Font(None, 86)
        self.normal = pygame.font.Font(None, 30)
        self.small = pygame.font.Font(None, 22)

    def text(self, surface, value, pos, font=None, color=WHITE, center=False):
        font = font or self.normal
        img = font.render(str(value), True, color)
        rect = img.get_rect()
        rect.center = pos if center else rect.center
        if not center:
            rect.topleft = pos
        surface.blit(img, rect)

    def panel(self, surface, rect, border=CYAN):
        pygame.draw.rect(surface, DARK, rect, border_radius=12)
        pygame.draw.rect(surface, border, rect, 2, border_radius=12)

    def menu(self, surface, pulse):
        self.text(surface, "NEON", (WIDTH//2, 150), self.title, CYAN, True)
        self.text(surface, "ESCAPE", (WIDTH//2, 220), self.title, MAGENTA, True)
        self.text(surface, "FUGA DA CIDADE", (WIDTH//2, 285), self.normal, WHITE, True)

        self.panel(surface, pygame.Rect(WIDTH//2-210, 350, 420, 130))
        self.text(surface, "ENTER  —  INICIAR", (WIDTH//2, 385), self.normal, GREEN, True)
        self.text(surface, "I  —  INSTRUÇÕES", (WIDTH//2, 425), self.normal, WHITE, True)
        self.text(surface, "ESC  —  SAIR", (WIDTH//2, 460), self.normal, GRAY, True)

    def instructions(self, surface):
        self.text(surface, "COMO JOGAR", (WIDTH//2, 120), self.big, CYAN, True)
        self.panel(surface, pygame.Rect(180, 175, 640, 330))
        lines = [
            "WASD ou SETAS  —  movimentar",
            "Colete os núcleos verdes para ganhar energia",
            "Colete os núcleos amarelos para ganhar bônus",
            "Evite os drones vermelhos",
            "A dificuldade aumenta com o tempo",
            "ESC  —  voltar ao menu",
        ]
        y = 225
        for line in lines:
            self.text(surface, line, (WIDTH//2, y), self.normal, WHITE, True)
            y += 43

    def hud(self, surface, player, level, remaining):
        pygame.draw.rect(surface, (10, 15, 35), (0, 0, WIDTH, 80))
        pygame.draw.line(surface, CYAN, (0, 79), (WIDTH, 79), 2)
        self.text(surface, f"PONTOS: {player.score}", (25, 18), self.normal, WHITE)
        self.text(surface, f"VIDAS: {player.lives}", (220, 18), self.normal, MAGENTA)
        self.text(surface, f"FASE: {level}", (380, 18), self.normal, CYAN)
        self.text(surface, f"TEMPO: {max(0, int(remaining))}", (520, 18), self.normal, YELLOW)

        pygame.draw.rect(surface, (40, 45, 65), (720, 24, 220, 24), border_radius=8)
        pygame.draw.rect(surface, GREEN, (720, 24, int(220*player.energy/100), 24), border_radius=8)
        self.text(surface, "ENERGIA", (830, 36), self.small, DARK, True)

    def centered_message(self, surface, title, subtitle, color):
        self.panel(surface, pygame.Rect(180, 190, 640, 260), color)
        self.text(surface, title, (WIDTH//2, 260), self.big, color, True)
        self.text(surface, subtitle, (WIDTH//2, 325), self.normal, WHITE, True)
        self.text(surface, "ENTER — reiniciar    ESC — menu", (WIDTH//2, 390), self.small, GRAY, True)
