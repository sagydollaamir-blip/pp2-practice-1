import pygame
import math
import datetime

center = (300, 300)

def draw_hand(screen, angle, length, color):
    x = center[0] + length * math.sin(angle)
    y = center[1] - length * math.cos(angle)
    pygame.draw.line(screen, color, center, (x, y), 5)

def draw_clock(screen):
    screen.fill((255, 255, 255))

    now = datetime.datetime.now()
    minutes = now.minute
    seconds = now.second

    min_angle = math.radians(minutes * 6)
    sec_angle = math.radians(seconds * 6)

    # minutes hand (right)
    draw_hand(screen, min_angle, 150, (0, 0, 0))

    # seconds hand (left)
    draw_hand(screen, sec_angle, 200, (255, 0, 0))

    pygame.draw.circle(screen, (0, 0, 0), center, 5)