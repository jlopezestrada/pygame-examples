import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Player")

# Font of the game
font = pygame.font.Font(None, 24)

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

    # Text on the screen
    # Health
    screen.blit(font.render("HEALTH", True, (255, 0, 0)), (10, 10))

    # XP
    screen.blit(font.render("XP", True, (255, 0, 0)), (10, 30))

    # Level
    screen.blit(font.render("LEVEL", True, (255, 0, 0)), (SCREEN_WIDTH - 80, 10))

    # Gold
    screen.blit(font.render("GOLD", True, (255, 0, 0)), (10, SCREEN_HEIGHT - 30))

    pygame.display.flip()

    clock.tick(60)

    # print(f"{clock.get_fps():.2f}")

pygame.quit()