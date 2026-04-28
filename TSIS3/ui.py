import pygame

class Button:
    def __init__(self, text, x, y, w, h):
        self.rect = pygame.Rect(x, y, w, h)
        self.text = text

    def draw(self, screen):
        pygame.draw.rect(screen, (100, 100, 100), self.rect)
        font = pygame.font.SysFont(None, 30)
        txt = font.render(self.text, True, (255,255,255))
        screen.blit(txt, (self.rect.x+20, self.rect.y+10))

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)