import pygame

pygame.init()

screen = pygame.display.set_mode((800,600))
clock = pygame.time.Clock()

color = (255,255,255)
mode = "draw"

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                mode = "rect"
            if event.key == pygame.K_c:
                mode = "circle"
            if event.key == pygame.K_e:
                mode = "eraser"

            if event.key == pygame.K_1:
                color = (255,0,0)
            if event.key == pygame.K_2:
                color = (0,255,0)
            if event.key == pygame.K_3:
                color = (0,0,255)
            if event.key == pygame.K_4:
                color = (255,255,255)

    mouse = pygame.mouse.get_pressed()
    pos = pygame.mouse.get_pos()

    if mouse[0]:
        if mode == "draw":
            pygame.draw.circle(screen, color, pos, 5)
        elif mode == "rect":
            pygame.draw.rect(screen, color, (*pos, 50, 50))
        elif mode == "circle":
            pygame.draw.circle(screen, color, pos, 30)
        elif mode == "eraser":
            pygame.draw.circle(screen, (0,0,0), pos, 10)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()