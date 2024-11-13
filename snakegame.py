import pygame
import random
import time

# Initialize pygame
pygame.init()

# Screen dimensions and setup
width, height = 600, 600
game_screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Jyothi Snake Game")

# Initial snake and food positions
snake_x, snake_y = width // 2, height // 2
change_x, change_y = 0, 0
snake_body = [(snake_x, snake_y)]
snake_size = 15

# Food settings
food_x, food_y = random.randrange(0, width, 10), random.randrange(0, height, 10)

# Colors
snake_color = (255, 255, 255)
food_color = (255, 192, 203)  # Pink color for food
background_color = (0, 0, 0)

# Game clock
clock = pygame.time.Clock()

# Function to display the snake and food, and check for game over
def display_snake_and_food():
    global snake_x, snake_y, food_x, food_y, snake_body

    # Update snake position
    snake_x = (snake_x + change_x) % width
    snake_y = (snake_y + change_y) % height

    # Check for collision with itself
    if (snake_x, snake_y) in snake_body[1:]:
        print("GAME OVER!!!")
        time.sleep(2)
        pygame.quit()
        quit()

    # Add new head to snake body
    snake_body.append((snake_x, snake_y))

    # Check if the snake has eaten the food
    if snake_x == food_x and snake_y == food_y:
        # Reposition food
        food_x, food_y = random.randrange(0, width, 5), random.randrange(0, height, 5)
    else:
        # Remove tail segment
        del snake_body[0]

    # Draw everything on the screen
    game_screen.fill(background_color)
    pygame.draw.rect(game_screen, food_color, [food_x, food_y, snake_size, snake_size])
    for (x, y) in snake_body:
        pygame.draw.rect(game_screen, snake_color, [x, y, snake_size, snake_size])
    pygame.display.update()

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and change_x == 0:
                change_x = -10
                change_y = 0
            elif event.key == pygame.K_RIGHT and change_x == 0:
                change_x = 10
                change_y = 0
            elif event.key == pygame.K_UP and change_y == 0:
                change_x = 0
                change_y = -10
            elif event.key == pygame.K_DOWN and change_y == 0:
                change_x = 0
                change_y = 10

    # Update the game display
    display_snake_and_food()
    clock.tick(12)

# Quit the game
pygame.quit()
