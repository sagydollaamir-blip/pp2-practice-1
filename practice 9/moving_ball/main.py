import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moving Ball")

x, y = 400, 300
radius = 25
speed = 20

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP] and y - speed - radius >= 0:
        y -= speed
    if keys[pygame.K_DOWN] and y + speed + radius <= HEIGHT:
        y += speed
    if keys[pygame.K_LEFT] and x - speed - radius >= 0:
        x -= speed
    if keys[pygame.K_RIGHT] and x + speed + radius <= WIDTH:
        x += speed

    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, (255, 0, 0), (x, y), radius)

    pygame.display.flip()
    clock.tick(60)