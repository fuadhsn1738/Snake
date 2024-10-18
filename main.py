import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Sound effect initialization (if you have a sound file, use it)
try:
    beep_sound = pygame.mixer.Sound(r"E:\Coding\Python\Game\Snake\point-smooth-beep-230573.mp3")
except pygame.error:
    beep_sound = None

# Constants
GAME_WIDTH = 1000
GAME_HEIGHT = 700
SPACE_SIZE = 25
BODY_PARTS = 3
SNAKE_COLOR = (0, 0, 255)  # Blue
FOOD_COLOR = (255, 255, 0)  # Yellow
BACKGROUND_COLOR = (0, 0, 0)  # Black
BASE_SPEED = 110  # Starting speed in ms
SPEED_INCREASE = 10  # Speed increment every 10 points

# Set up display
screen = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
pygame.display.set_caption('Snake Imprezia')

# Fonts for displaying score, game over, and title screen
font = pygame.font.SysFont("consolas", 40)
game_over_font = pygame.font.SysFont("consolas", 70)
title_font = pygame.font.SysFont("consolas", 80)

# Initialize clock
clock = pygame.time.Clock()

class Snake:
    def __init__(self):
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []

        # Initialize snake's body in the top-left corner
        for i in range(0, BODY_PARTS):
            self.coordinates.append([0, 0])

    def draw(self):
        for x, y in self.coordinates:
            pygame.draw.rect(screen, SNAKE_COLOR, pygame.Rect(x, y, SPACE_SIZE, SPACE_SIZE))

class Food:
    def __init__(self):
        self.coordinates = self.generate_food_position()

    def generate_food_position(self):
        x = random.randint(0, (GAME_WIDTH // SPACE_SIZE) - 1) * SPACE_SIZE
        y = random.randint(0, (GAME_HEIGHT // SPACE_SIZE) - 1) * SPACE_SIZE
        return [x, y]

    def draw(self):
        pygame.draw.ellipse(screen, FOOD_COLOR, pygame.Rect(self.coordinates[0], self.coordinates[1], SPACE_SIZE, SPACE_SIZE))

def draw_text(text, font, color, position):
    label = font.render(text, True, color)
    screen.blit(label, position)

def next_turn(snake, food):
    # Get the current head position of the snake
    x, y = snake.coordinates[0]

    # Update the position based on the direction
    if direction == "up":
        y -= SPACE_SIZE
    elif direction == "down":
        y += SPACE_SIZE
    elif direction == "left":
        x -= SPACE_SIZE
    elif direction == "right":
        x += SPACE_SIZE

    # Implement screen wrapping logic
    if x < 0:
        x = GAME_WIDTH - SPACE_SIZE
    elif x >= GAME_WIDTH:
        x = 0
    if y < 0:
        y = GAME_HEIGHT - SPACE_SIZE
    elif y >= GAME_HEIGHT:
        y = 0

    # Insert the new head position
    snake.coordinates.insert(0, [x, y])

    # Check if the snake eats the food
    if x == food.coordinates[0] and y == food.coordinates[1]:
        global score, current_speed
        score += 1

        # Play beep sound when snake eats food
        if beep_sound:
            beep_sound.play()

        # Create new food
        food.coordinates = food.generate_food_position()

        # Increase speed every 10 points
        if score % 10 == 0:
            current_speed = max(10, current_speed - SPEED_INCREASE)  # Ensure minimum speed
    else:
        # Remove the tail if no food is eaten
        snake.coordinates.pop()

    # Check for self-collision
    if check_collision(snake):
        return False

    return True

def check_collision(snake):
    head = snake.coordinates[0]
    for segment in snake.coordinates[1:]:
        if head == segment:
            return True
    return False

def game_over():
    screen.fill(BACKGROUND_COLOR)
    draw_text("Game Over", game_over_font, (255, 0, 0), (GAME_WIDTH // 2 - 150, GAME_HEIGHT // 2 - 50))
    draw_text("Press R to Restart", font, (255, 255, 255), (GAME_WIDTH // 2 - 200, GAME_HEIGHT // 2 + 50))
    pygame.display.flip()

def restart_game():
    global snake, food, score, direction, current_speed
    snake = Snake()
    food = Food()
    score = 0
    direction = "down"
    current_speed = BASE_SPEED

def title_screen():
    screen.fill(BACKGROUND_COLOR)
    draw_text("Snake Imprezia", title_font, (255, 255, 255), (GAME_WIDTH // 2 - 300, GAME_HEIGHT // 2 - 100))
    draw_text("Press Any Key to Start", font, (255, 255, 255), (GAME_WIDTH // 2 - 230, GAME_HEIGHT // 2 + 50))
    pygame.display.flip()

    # Wait for the player to press any key to start
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                waiting = False

# Game setup
snake = Snake()
food = Food()
score = 0
direction = "down"
current_speed = BASE_SPEED

# Show title screen
title_screen()

# Main game loop
running = True
while running:
    screen.fill(BACKGROUND_COLOR)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != "down":
                direction = "up"
            if event.key == pygame.K_DOWN and direction != "up":
                direction = "down"
            if event.key == pygame.K_LEFT and direction != "right":
                direction = "left"
            if event.key == pygame.K_RIGHT and direction != "left":
                direction = "right"
            if event.key == pygame.K_r:
                restart_game()

    # Update game state
    if not next_turn(snake, food):
        game_over()
        while True:
            event = pygame.event.wait()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                restart_game()
                break
            if event.type == pygame.QUIT:
                running = False
                break

    # Draw everything
    snake.draw()
    food.draw()
    draw_text(f"Score: {score}", font, (255, 255, 255), (10, 10))

    # Refresh screen
    pygame.display.update()

    # Control game speed
    pygame.time.delay(current_speed)

# Quit the game
pygame.quit()
sys.exit()
