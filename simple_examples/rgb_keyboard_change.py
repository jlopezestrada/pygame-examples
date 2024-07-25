import pygame

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
            screen.fill((255, 0, 0))

        elif event.type == pygame.KEYUP:
            screen.fill((0, 0, 0))

    pygame.display.flip()

    clock.tick(60)

    # Display FPS for debugging
    print(f"FPS: {clock.get_fps():.2f}")