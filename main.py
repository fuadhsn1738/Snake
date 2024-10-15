from tkinter import *
import random

# Constants
GAME_WIDTH = 700
GAME_HEIGHT = 500
SPEED = 50
SPACE_SIZE = 50
BODY_PARTS = 3
SNAKE_COLOR = "#00FF00"
FOOD_COLOR = "#FF0000"
BACKGROUND_COLOR = "#000000"

class Snake:
    def __init__(self):
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []

        # Initialize the snake's body
        for i in range(0, BODY_PARTS):
            self.coordinates.append([0, 0])

            for x, y in self.coordinates:
                square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tag="snake")
                self.squares.append(square)

class Food:
    def __init__(self):
        # Randomly place the food on the canvas
        x = random.randint(0, int(GAME_WIDTH / SPACE_SIZE) - 1) * SPACE_SIZE
        y = random.randint(0, int(GAME_HEIGHT / SPACE_SIZE) - 1) * SPACE_SIZE

        self.coordinates = [x, y]

        # Create the food item on the canvas
        canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tag="food")

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
    
    # Insert the new head position
    snake.coordinates.insert(0, (x, y))

    # Create a new square for the snake's head
    square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR)
    snake.squares.insert(0, square)

    # Remove the last part of the snake's body
    del snake.coordinates[-1]
    canvas.delete(snake.squares[-1])
    del snake.squares[-1]

    # Schedule the next turn
    window.after(SPEED, next_turn, snake, food)

def change_direction(new_direction):
    # Placeholder for changing direction logic
    pass

def check_collision():
    # Placeholder for collision detection logic
    pass

def game_over():
    # Placeholder for game over logic
    pass

# Initialize the main window
window = Tk()
window.title("Snake Imprezia")
window.resizable(True, True)

# Initialize the score and direction
score = 0
direction = "down"

# Create and pack the score label
label = Label(window, text="Score: {}".format(score), font=('consolas', 40))
label.pack()

# Create and pack the canvas
canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

# Update the window to get its dimensions
window.update()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Center the window on the screen
x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))
window.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Create the snake and food objects
snake = Snake()
food = Food()

# Start the game loop
next_turn(snake, food)

# Run the main loop
window.mainloop()