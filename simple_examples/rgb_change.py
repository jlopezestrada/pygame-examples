import pygame

pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# System clock
clock = pygame.time.Clock()

# Init the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("RGB Change")

# Colors array
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]
color_index = 0

# Change colors
change_colors = pygame.time.get_ticks()
color_change_time = 500 # ms

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("Exit game.")
            running = False

    if pygame.time.get_ticks() - change_colors >= color_change_time:
        color_index = (color_index + 1) % len(colors)
        change_colors = pygame.time.get_ticks()

    screen.fill(colors[color_index])
    pygame.display.flip()

    clock.tick(60)

    # Display FPS for debugging
    print(f"FPS: {clock.get_fps():.2f}")