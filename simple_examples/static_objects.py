import pygame

pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Static object 1
RECT_WIDTH = 40
RECT_HEIGHT = 30

# Static object 2
OBJ_WIDTH = 70
OBJ_HEIGHT = 50

# Init the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Static Objects")

# Clock
clock = pygame.time.Clock()

running = True

while running:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    pygame.draw.rect(screen, (255, 0, 255), (400, 400, RECT_WIDTH, RECT_HEIGHT))
    pygame.draw.rect(screen, (255, 255, 0), (200, 400, OBJ_WIDTH, OBJ_HEIGHT))

    pygame.display.flip()

    clock.tick(60)  