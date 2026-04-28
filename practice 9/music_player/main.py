import pygame
import sys
from player import MusicPlayer

pygame.init()

screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Music Player")

player = MusicPlayer()

font = pygame.font.Font(None, 36)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                player.play()
            elif event.key == pygame.K_s:
                player.stop()
            elif event.key == pygame.K_n:
                player.next()
            elif event.key == pygame.K_b:
                player.prev()

    screen.fill((200, 200, 200))

    text = font.render(f"Track: {player.get_current()}", True, (0, 0, 0))
    screen.blit(text, (50, 150))

    pygame.display.flip()