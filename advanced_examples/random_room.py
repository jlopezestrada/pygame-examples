import pygame
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Random Room")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill((0, 128, 255))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = 5
        self.health = 5

    def update(self, keys_pressed):
        if keys_pressed[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys_pressed[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.x += self.speed
        if keys_pressed[pygame.K_UP] and self.rect.top > 0:
            self.rect.y -= self.speed
        if keys_pressed[pygame.K_DOWN] and self.rect.bottom < HEIGHT:
            self.rect.y += self.speed

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = 2

    def update(self, player_pos):
        if self.rect.x < player_pos[0]:
            self.rect.x += self.speed
        elif self.rect.x > player_pos[0]:
            self.rect.x -= self.speed

        if self.rect.y < player_pos[1]:
            self.rect.y += self.speed
        elif self.rect.y > player_pos[1]:
            self.rect.y -= self.speed

class Item(pygame.sprite.Sprite):
    def __init__(self, x, y, effect):
        super().__init__()
        self.image = pygame.Surface((20, 20))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.effect = effect

def generate_room():
    enemies = pygame.sprite.Group()
    items = pygame.sprite.Group()
    num_enemies = random.randint(1, 5)
    num_items = random.randint(0, 2)

    for _ in range(num_enemies):
        x = random.randint(50, WIDTH - 50)
        y = random.randint(50, HEIGHT - 50)
        enemy = Enemy(x, y)
        enemies.add(enemy)

    for _ in range(num_items):
        x = random.randint(50, WIDTH - 50)
        y = random.randint(50, HEIGHT - 50)
        item = Item(x, y, effect='heal')
        items.add(item)

    return enemies, items

def main():
    clock = pygame.time.Clock()
    run = True

    player = Player(WIDTH // 2, HEIGHT // 2)
    player_group = pygame.sprite.Group()
    player_group.add(player)

    enemies, items = generate_room()

    while run:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys_pressed = pygame.key.get_pressed()
        player.update(keys_pressed)

        enemies.update(player.rect.center)

        if pygame.sprite.spritecollide(player, enemies, False):
            player.health -= 1
            if player.health <= 0:
                print("Game Over!")
                run = False
            else:
                enemies.empty()
                items.empty()
                enemies, items = generate_room()
                player.rect.center = (WIDTH // 2, HEIGHT // 2)

        item_collisions = pygame.sprite.spritecollide(player, items, True)
        for item in item_collisions:
            if item.effect == 'heal':
                player.health += 1

        WINDOW.fill(BLACK)

        player_group.draw(WINDOW)
        enemies.draw(WINDOW)
        items.draw(WINDOW)

        font = pygame.font.SysFont(None, 36)
        health_text = font.render(f'Health: {player.health}', True, WHITE)
        WINDOW.blit(health_text, (10, 10))

        # Update the display
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
