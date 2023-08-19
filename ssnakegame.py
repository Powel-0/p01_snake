import pygame
import random

# Initialize pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 640, 480
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Snake properties
snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]
snake_dir = 'RIGHT'
change_to = snake_dir

# Food properties
food_pos = [random.randrange(1, (WIDTH // 10)) * 10,
            random.randrange(1, (HEIGHT // 10)) * 10]
food_spawn = True

# Game over
game_over = False

# FPS (frames per second) controller
fps = pygame.time.Clock()

# Main game loop
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'

    # Validation of direction
    if change_to == 'UP' and not snake_dir == 'DOWN':
        snake_dir = 'UP'
    if change_to == 'DOWN' and not snake_dir == 'UP':
        snake_dir = 'DOWN'
    if change_to == 'LEFT' and not snake_dir == 'RIGHT':
        snake_dir = 'LEFT'
    if change_to == 'RIGHT' and not snake_dir == 'LEFT':
        snake_dir = 'RIGHT'

    # Moving the snake
    if snake_dir == 'UP':
        snake_pos[1] -= 10
    if snake_dir == 'DOWN':
        snake_pos[1] += 10
    if snake_dir == 'LEFT':
        snake_pos[0] -= 10
    if snake_dir == 'RIGHT':
        snake_pos[0] += 10

    # Snake body growing mechanism
    snake_body.insert(0, list(snake_pos))
    if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
        food_spawn = False
    else:
        snake_body.pop()

    if not food_spawn:
        food_pos = [random.randrange(1, (WIDTH // 10)) * 10,
                    random.randrange(1, (HEIGHT // 10)) * 10]
    food_spawn = True

    # Draw snake and food
    win.fill(WHITE)
    for pos in snake_body:
        pygame.draw.rect(win, GREEN, pygame.Rect(pos[0], pos[1], 10, 10))

    pygame.draw.rect(win, RED, pygame.Rect(
        food_pos[0], food_pos[1], 10, 10))

    # Game Over conditions
    if snake_pos[0] < 0 or snake_pos[0] > WIDTH - 10:
        game_over = True
    if snake_pos[1] < 0 or snake_pos[1] > HEIGHT - 10:
        game_over = True
    for block in snake_body[1:]:
        if snake_pos[0] == block[0] and snake_pos[1] == block[1]:
            game_over = True

    # Refresh screen
    pygame.display.update()
    fps.tick(15)

# Quit pygame
