from tkinter import *
import random

# Constants
GAME_WIDTH = 1000
GAME_HEIGHT = 700
SPEED = 110
SPACE_SIZE = 25
BODY_PARTS = 3
SNAKE_COLOR = "#0000FF"
FOOD_COLOR = "#FFFF00"
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
    # Ensure snake has coordinates
    if not snake.coordinates:
        return
    
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

    if x == food.coordinates[0] and y == food.coordinates[1]:
        # The snake has eaten the food
        global score
        score += 1
        label.config(text="Score: {}".format(score))

        # Remove the food item from the canvas
        canvas.delete("food")

        # Create a new food item
        food = Food()

    else:
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]
    
    if check_collision(snake):
        game_over()
    else:
        window.after(SPEED, next_turn, snake, food)


def change_direction(new_direction):
    global direction

    # Prevent the snake from reversing
    if new_direction == "left":
        if direction != "right":
            direction = new_direction
    elif new_direction == "right":
        if direction != "left":
            direction = new_direction
    elif new_direction == "up":
        if direction != "down":
            direction = new_direction
    elif new_direction == "down":
        if direction != "up":
            direction = new_direction
    

def check_collision(snake):
    x, y = snake.coordinates[0]

    # Check if the snake has collided with the walls or itself
    if x < 0 or x >= GAME_WIDTH:
        return True
    
    elif y < 0 or y >= GAME_HEIGHT:
        return True
    
    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            return True
    
    return False # No collision

def game_over():
    global restart_button
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width() / 2, canvas.winfo_height() / 2,
<<<<<<< Updated upstream
                       font=('consolas', 70), text="Game Over",
                       fill="red", anchor="center", tag="gameover")
    
    # Create the restart button and place it on the canvas
=======
                        font=('consolas', 70), text="Game Over",
                          fill="red", anchor="center", tag="gameover")
>>>>>>> Stashed changes
    restart_button = Button(window, text="Restart", command=restart_game)
    restart_button.pack()

def restart_game():
    global snake, food, score, direction, restart_button
    canvas.delete(ALL)
    score = 0
    direction = "down"
    label.config(text="Score: {}".format(score))
    snake = Snake()
    food = Food()
    next_turn(snake, food)
    restart_button.destroy()

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

# Bind the arrow keys to the change_direction function
window.bind("<Up>", lambda event: change_direction("up"))
window.bind("<Down>", lambda event: change_direction("down"))
window.bind("<Left>", lambda event: change_direction("left"))
window.bind("<Right>", lambda event: change_direction("right"))

# Create the snake and food objects
snake = Snake()
food = Food()

# Start the game loop
next_turn(snake, food)

# Run the main loop
window.mainloop()