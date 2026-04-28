import pygame
import random

class Player:
    def __init__(self):
        self.x = 250
        self.y = 600
        self.speed = 5
        self.rect = pygame.Rect(self.x, self.y, 50, 80)

    def move(self, keys):
        if keys[pygame.K_LEFT]:
            self.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.x += self.speed

        self.rect.topleft = (self.x, self.y)

    def draw(self, screen):
        pygame.draw.rect(screen, (0, 255, 0), self.rect)


class TrafficCar:
    def __init__(self):
        self.x = random.choice([150, 250, 350])
        self.y = -100
        self.speed = 5
        self.rect = pygame.Rect(self.x, self.y, 50, 80)

    def update(self):
        self.y += self.speed
        self.rect.topleft = (self.x, self.y)

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), self.rect)


class RacerGame:
    def __init__(self, settings):
        self.player = Player()
        self.cars = []
        self.spawn_timer = 0

        self.distance = 0
        self.score = 0

    def update(self, screen):
        keys = pygame.key.get_pressed()
        self.player.move(keys)

        # spawn traffic
        self.spawn_timer += 1
        if self.spawn_timer > 60:
            self.cars.append(TrafficCar())
            self.spawn_timer = 0

        # update cars
        for car in self.cars:
            car.update()
            if car.rect.colliderect(self.player.rect):
                return "game_over"

        # remove off-screen cars
        self.cars = [c for c in self.cars if c.y < 800]

        # update score
        self.distance += 1
        self.score = self.distance // 5

        # draw
        screen.fill((50, 50, 50))
        self.player.draw(screen)

        for car in self.cars:
            car.draw(screen)

        return "running"