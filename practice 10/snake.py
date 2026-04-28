import pygame
import random

pygame.init()

WIDTH, HEIGHT = 400, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

snake = [(200,200)]
dx, dy = 20, 0
food = (100,100)

score = 0
level = 1
speed = 10

def new_food():
    while True:
        f = (random.randrange(0, WIDTH, 20),
             random.randrange(0, HEIGHT, 20))
        if f not in snake:
            return f

running = True
while running:
    screen.fill((0,0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]: dx, dy = 0, -20
    if keys[pygame.K_DOWN]: dx, dy = 0, 20
    if keys[pygame.K_LEFT]: dx, dy = -20, 0
    if keys[pygame.K_RIGHT]: dx, dy = 20, 0

    head = (snake[0][0] + dx, snake[0][1] + dy)

    # collision with wall
    if not (0 <= head[0] < WIDTH and 0 <= head[1] < HEIGHT):
        running = False

    snake.insert(0, head)

    if head == food:
        score += 1
        food = new_food()

        if score % 3 == 0:
            level += 1
            speed += 2
    else:
        snake.pop()

    for s in snake:
        pygame.draw.rect(screen, (0,255,0), (*s,20,20))

    pygame.draw.rect(screen, (255,0,0), (*food,20,20))

    pygame.display.flip()
    clock.tick(speed)

pygame.quit()