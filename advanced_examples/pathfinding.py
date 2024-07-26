import pygame
import heapq
import random

pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
CELL_SIZE = 20
GRID_WIDTH = SCREEN_WIDTH // CELL_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // CELL_SIZE

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pathfinding")

# Create a 2D grid
grid = [[0 for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]

# Generate obstacles
def generate_maze():
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            grid[y][x] = 1
    
    def carve_path(x, y):
        grid[y][x] = 0
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        random.shuffle(directions)
        for dx, dy in directions:
            nx, ny = x + dx*2, y + dy*2
            if 0 <= nx < GRID_WIDTH and 0 <= ny < GRID_HEIGHT and grid[ny][nx] == 1:
                grid[y+dy][x+dx] = 0
                carve_path(nx, ny)

    start_x, start_y = random.randint(0, GRID_WIDTH-1), random.randint(0, GRID_HEIGHT-1)
    carve_path(start_x, start_y)

    # More random passages
    for _ in range(GRID_WIDTH * GRID_HEIGHT // 10):
        x, y = random.randint(1, GRID_WIDTH-2), random.randint(1, GRID_HEIGHT-2)
        grid[y][x] = 0

generate_maze()

def heuristic(a, b):
    return abs(b[0] - a[0]) + abs(b[1] - a[1])

def a_star(start, goal):
    neighbors = [(0,1), (0,-1), (1,0), (-1,0)]
    close_set = set()
    came_from = {}
    gscore = {start:0}
    fscore = {start:heuristic(start, goal)}
    open_heap = []
    heapq.heappush(open_heap, (fscore[start], start))
    
    while open_heap:
        current = heapq.heappop(open_heap)[1]
        
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return path

        close_set.add(current)
        
        for i, j in neighbors:
            neighbor = current[0] + i, current[1] + j
            tentative_g_score = gscore[current] + 1
            if 0 <= neighbor[0] < GRID_HEIGHT and 0 <= neighbor[1] < GRID_WIDTH:
                if grid[neighbor[0]][neighbor[1]] == 1:
                    continue
            else:
                continue
                
            if neighbor in close_set and tentative_g_score >= gscore.get(neighbor, 0):
                continue
                
            if tentative_g_score < gscore.get(neighbor, 0) or neighbor not in [i[1]for i in open_heap]:
                came_from[neighbor] = current
                gscore[neighbor] = tentative_g_score
                fscore[neighbor] = gscore[neighbor] + heuristic(neighbor, goal)
                heapq.heappush(open_heap, (fscore[neighbor], neighbor))
    
    return False

# Main game loop
start = None
goal = None
path = None
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            grid_x, grid_y = x // CELL_SIZE, y // CELL_SIZE
            if event.button == 1:
                if grid[grid_y][grid_x] == 0:
                    if not start:
                        start = (grid_y, grid_x)
                    elif not goal:
                        goal = (grid_y, grid_x)
                        path = a_star(start, goal)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                generate_maze()
                start = None
                goal = None
                path = None

    # Draw grid
    screen.fill(WHITE)
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            if grid[y][x] == 1:
                pygame.draw.rect(screen, BLACK, rect)
            else:
                pygame.draw.rect(screen, WHITE, rect, 1)

    # Draw start and goal
    if start:
        pygame.draw.rect(screen, GREEN, (start[1] * CELL_SIZE, start[0] * CELL_SIZE, CELL_SIZE, CELL_SIZE))
    if goal:
        pygame.draw.rect(screen, RED, (goal[1] * CELL_SIZE, goal[0] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    # Draw path
    if path:
        for cell in path:
            pygame.draw.rect(screen, BLUE, (cell[1] * CELL_SIZE, cell[0] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    pygame.display.flip()

pygame.quit()