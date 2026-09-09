import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
dt = 0.0


while True:
    dt = clock.tick(60) / 1000
    print(dt)
    log_state()
    for event in pygame.event.get():
        pass

    screen.fill("black")
    pygame.display.flip()
