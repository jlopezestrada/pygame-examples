import pygame

pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Enemy AI")
clock = pygame.time.Clock()

# Player
PLAYER_WIDTH = 50
PLAYER_HEIGHT = 50
mov_x_player = SCREEN_WIDTH / 2
mov_y_player = SCREEN_HEIGHT / 2
speed_player = 10

# Enemies
ENEMY_ONE_RADIUS = 15
ENEMY_TWO_RADIUS = 15
mov_x_enemy_one = SCREEN_WIDTH / 4
mov_y_enemy_one = SCREEN_HEIGHT / 4
mov_x_enemy_two = SCREEN_WIDTH / 3
mov_y_enemy_two = SCREEN_HEIGHT / 3
enemy_speed = 5

def enemy_move_player(enemy_x, enemy_y, player_x, player_y, other_enemy_x, other_enemy_y, speed):
    dx = player_x - enemy_x
    dy = player_y - enemy_y
    distance = (dx**2 + dy**2) ** 0.5

    if distance != 0:
        dx = (dx / distance) * speed
        dy = (dy / distance) * speed
    else:
        dx = dy = 0

    separation_x = enemy_x - other_enemy_x
    separation_y = enemy_y - other_enemy_y
    separation_distance = (separation_x**2 + separation_y**2) ** 0.5

    if separation_distance < ENEMY_ONE_RADIUS * 3:
        dx += separation_x / separation_distance
        dy += separation_y / separation_distance

    return enemy_x + dx, enemy_y + dy

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    keys_pressed = pygame.key.get_pressed()

    # Player movement
    if keys_pressed[pygame.K_w] and mov_y_player > 0:
        mov_y_player -= speed_player
    if keys_pressed[pygame.K_s] and mov_y_player < SCREEN_HEIGHT - PLAYER_HEIGHT:
        mov_y_player += speed_player 
    if keys_pressed[pygame.K_a] and mov_x_player > 0:
        mov_x_player -= speed_player 
    if keys_pressed[pygame.K_d] and mov_x_player < SCREEN_WIDTH - PLAYER_WIDTH:
        mov_x_player += speed_player

    mov_x_enemy_one, mov_y_enemy_one = enemy_move_player(mov_x_enemy_one, mov_y_enemy_one, mov_x_player, mov_y_player, mov_x_enemy_two, mov_y_enemy_two, enemy_speed)
    mov_x_enemy_two, mov_y_enemy_two = enemy_move_player(mov_x_enemy_two, mov_y_enemy_two, mov_x_player, mov_y_player, mov_x_enemy_one, mov_y_enemy_one, enemy_speed)   

    mov_x_enemy_one = max(ENEMY_ONE_RADIUS, min(SCREEN_WIDTH - ENEMY_ONE_RADIUS, mov_x_enemy_one))
    mov_y_enemy_one = max(ENEMY_ONE_RADIUS, min(SCREEN_WIDTH - ENEMY_ONE_RADIUS, mov_y_enemy_one))
    mov_x_enemy_two = max(ENEMY_TWO_RADIUS, min(SCREEN_WIDTH - ENEMY_TWO_RADIUS, mov_x_enemy_two))
    mov_y_enemy_two = max(ENEMY_TWO_RADIUS, min(SCREEN_WIDTH - ENEMY_TWO_RADIUS, mov_y_enemy_two))

    pygame.draw.rect(screen, (255, 255, 255), (mov_x_player, mov_y_player, PLAYER_HEIGHT, PLAYER_HEIGHT))
    pygame.draw.circle(screen, (255, 0, 0), (mov_x_enemy_one, mov_y_enemy_one), ENEMY_ONE_RADIUS)
    pygame.draw.circle(screen, (255, 0, 0), (mov_x_enemy_two, mov_y_enemy_two), ENEMY_TWO_RADIUS)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()