import pygame
import time

pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# System clock
clock = pygame.time.Clock()

# Init the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Moba")

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("Exit game.")
            running = False
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                screen.fill((255, 0, 0))
            elif event.key == pygame.K_g:
                screen.fill((0, 255, 0))
            elif event.key == pygame.K_b:
                screen.fill((0, 0, 255))
            pygame.display.flip()

        elif event.type == pygame.KEYUP:
            screen.fill((0, 0, 0))
            pygame.display.flip()

    clock.tick(60)