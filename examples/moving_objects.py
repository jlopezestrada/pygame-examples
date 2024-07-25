import pygame

pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Moving object 1 (rectangle)
OBJ_WIDTH = 40
OBJ_HEIGHT = 30
mov_x = SCREEN_WIDTH / 2
mov_y = SCREEN_HEIGHT / 2
obj_speed = 10

# Moving object 2 (circle)
CIRCLE_RADIUS = 40
mov_x_circle = SCREEN_WIDTH / 3
mov_y_circle = SCREEN_HEIGHT / 3
circle_speed = 8

# Init the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Moving Objects")

# Clock
clock = pygame.time.Clock()

running = True

while running:
    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    key_pressed = pygame.key.get_pressed() # pygame.key.get_pressed() returns an array of booleans with the pressed keys in the keyboard
    # if instead of elif to handle multiple key movements https://docs.python.org/3/tutorial/controlflow.html
    if key_pressed[pygame.K_w] and mov_y > 0:
        mov_y -= obj_speed
    if key_pressed[pygame.K_s] and mov_y < SCREEN_HEIGHT - OBJ_HEIGHT:
        mov_y += obj_speed
    if key_pressed[pygame.K_a] and mov_x > 0:
        mov_x -= obj_speed
    if key_pressed[pygame.K_d] and mov_x < SCREEN_WIDTH - OBJ_WIDTH:
        mov_x += obj_speed

    if key_pressed[pygame.K_UP] and mov_y_circle > CIRCLE_RADIUS:
        mov_y_circle -= circle_speed
    if key_pressed[pygame.K_DOWN] and mov_y_circle < SCREEN_HEIGHT - CIRCLE_RADIUS:
        mov_y_circle += circle_speed
    if key_pressed[pygame.K_LEFT] and mov_x_circle > CIRCLE_RADIUS:
        mov_x_circle -= circle_speed
    if key_pressed[pygame.K_RIGHT] and mov_x_circle < SCREEN_WIDTH - CIRCLE_RADIUS:
        mov_x_circle += circle_speed

    pygame.draw.rect(screen, (255, 255, 255), (mov_x, mov_y, OBJ_WIDTH, OBJ_HEIGHT))
    pygame.draw.circle(screen, (255, 0, 255), (int(mov_x_circle), int(mov_y_circle)), CIRCLE_RADIUS)

    pygame.display.flip()

    clock.tick(60)    