import pygame
import random

pygame.init()

WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

player = pygame.Rect(180, 500, 40, 60)
coins = []
score = 0

font = pygame.font.SysFont(None, 30)

def spawn_coin():
    x = random.randint(0, WIDTH - 20)
    return pygame.Rect(x, 0, 20, 20)

running = True
while running:
    screen.fill((30, 30, 30))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.x -= 5
    if keys[pygame.K_RIGHT]:
        player.x += 5

    if random.randint(1, 50) == 1:
        coins.append(spawn_coin())

    for coin in coins[:]:
        coin.y += 5
        if player.colliderect(coin):
            coins.remove(coin)
            score += 1

    pygame.draw.rect(screen, (0, 255, 0), player)

    for coin in coins:
        pygame.draw.rect(screen, (255, 255, 0), coin)

    text = font.render(f"Coins: {score}", True, (255,255,255))
    screen.blit(text, (280, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()