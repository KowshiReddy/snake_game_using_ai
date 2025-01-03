import pygame
import random
import time

# Initialize Pygame
pygame.mixer.init()
pygame.init()

pygame.mixer.music.load("C:/Users/reddy/Downloads/squid-game-music-tone.mp3")  
game_over_sound="C:/Users/reddy/Downloads/game-over-160612.mp3"
pygame.mixer.music.play(-1)  # Loops indefinitely

# Game Window Dimensions
WIDTH, HEIGHT = 800, 600
CELL_SIZE = 10

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Initialize Game Window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")


level = 1
speed = 10  # Snake speed (gamespeed increases at each level)

# Increase game speed as the player progresses
def increase_level(score):
    global level, speed
    level = score // 5 + 1  # Increase level every 5 points
    speed = 10 + level      # Adjust speed, gets faster at higher levels


# Clock for controlling the game speed
clock = pygame.time.Clock()

def show_text(text, pos, size, color):
    """
    Helper function to render text on the screen.
    """
    font = pygame.font.Font(None, size)
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, pos)

def place_food():
    """
    Generate a random position for food within the game boundaries.
    """
    x = random.randint(0, (WIDTH // CELL_SIZE) - 1) * CELL_SIZE
    y = random.randint(0, (HEIGHT // CELL_SIZE) - 1) * CELL_SIZE
    return x, y

def draw_snake(snake):
    """
    Draw the snake on the screen.
    """
    for segment in snake:
        pygame.draw.rect(screen, GREEN, pygame.Rect(segment[0], segment[1], CELL_SIZE, CELL_SIZE))

def check_collision(head, snake):
    """
    Check for collisions with the snake body or walls.
    """
    # Check wall collisions
    if head[0] < 0 or head[0] >= WIDTH or head[1] < 0 or head[1] >= HEIGHT:
        return True

    # Check self-collision
    if head in snake[1:]:
        return True

    return False

def show_start_screen():
    screen.fill(BLACK)
    show_text("Welcome to Snake Game!", (WIDTH // 3-100, HEIGHT // 3 - 60), 60, GREEN)
    show_text("Press Enter to Start", (WIDTH // 3, HEIGHT // 3), 30, WHITE)

    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    waiting = False


def show_menu():
    """
    Display the 'Game Over' screen with 'Try Again' option.
    Wait for the user's input to restart or quit.
    """
    screen.fill(BLACK)
    show_text("Game Over!", (WIDTH // 2 - 100, HEIGHT // 2 - 60), 50, RED)
    show_text(f"Your Score: {score}", (WIDTH // 2 - 90, HEIGHT // 2 - 10), 40, WHITE)
    show_text("Press Enter to Try Again or Esc to Quit", (WIDTH // 2 - 160, HEIGHT // 2 + 40), 30, WHITE)
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:  # Enter restarts the game
                    return True
                elif event.key == pygame.K_ESCAPE:  # Esc quits the game
                    pygame.quit()
                    exit()

# Main Game Loop

show_start_screen()
running = True
while running:
    # Initialize Game Variables
    snake = [(100, 100), (90, 100), (80, 100)]
    direction = 'RIGHT'
    food_pos = place_food()
    score = 0

    while True:
        screen.fill(BLACK)
        
        # Event Handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                
                pygame.quit()
                exit()

        # Control Snake Direction
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and direction != 'DOWN':
            direction = 'UP'
        if keys[pygame.K_DOWN] and direction != 'UP':
            direction = 'DOWN'
        if keys[pygame.K_LEFT] and direction != 'RIGHT':
            direction = 'LEFT'
        if keys[pygame.K_RIGHT] and direction != 'LEFT':
            direction = 'RIGHT'

        # Move Snake
        head = snake[0]
        if direction == 'UP':
            new_head = (head[0], head[1] - CELL_SIZE)
        elif direction == 'DOWN':
            new_head = (head[0], head[1] + CELL_SIZE)
        elif direction == 'LEFT':
            new_head = (head[0] - CELL_SIZE, head[1])
        elif direction == 'RIGHT':
            new_head = (head[0] + CELL_SIZE, head[1])

        snake.insert(0, new_head)

        # Check for Food Collision
        if new_head == food_pos:
            score += 1
            food_pos = place_food()
            increase_level(score)
        else:
            snake.pop()

        # Check for Collisions
        if check_collision(new_head, snake):
            pygame.mixer.music.stop()
            pygame.mixer.music.load(game_over_sound)
            pygame.mixer.music.play()
            if show_menu():
                break
            else:
                running = False
                break

        # Draw Everything
        draw_snake(snake)
        pygame.draw.rect(screen, RED, pygame.Rect(food_pos[0], food_pos[1], CELL_SIZE, CELL_SIZE))
        show_text(f"Score: {score}", (10, 10), 30, WHITE)

        pygame.display.flip()
        clock.tick(10)

