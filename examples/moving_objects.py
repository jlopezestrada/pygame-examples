import pygame
import time

pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Moving object 1
OBJ_WIDTH = 40
OBJ_HEIGHT = 30

# Init the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Moving Objects")

# Clock
clock = pygame.time.Clock()

running = True

while running:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            running = False

    pygame.draw.rect(screen, (255, 255, 255), (400, 400, OBJ_WIDTH, OBJ_HEIGHT))

    clock.tick(60)    

    pygame.display.flip()