import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Player")

# Clock
clock = pygame.time.Clock()

# Player
PLAYER_WIDTH = 50
PLAYER_HEIGHT = 50
player_x = SCREEN_WIDTH / 2
player_y = SCREEN_HEIGHT / 2
player_speed = 8

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_w] and player_y > 0:
        player_y -= player_speed 
    if keys[pygame.K_s] and player_y < SCREEN_HEIGHT - PLAYER_HEIGHT:
        player_y += player_speed 
    if keys[pygame.K_a] and player_x > 0:
        player_x -= player_speed 
    if keys[pygame.K_d] and player_x < SCREEN_WIDTH - PLAYER_WIDTH:
        player_x += player_speed 

    # Create the player
    pygame.draw.rect(screen, (255, 0, 255), (player_x, player_y, PLAYER_WIDTH, PLAYER_HEIGHT))

    pygame.display.flip()

    clock.tick(60)

    # print(f"{clock.get_fps():.2f}")

pygame.quit()