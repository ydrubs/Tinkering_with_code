import turtle
import random

# Constants
CELL_SIZE = 20
ROWS = 20
COLS = 20

# Function to draw a rectangle
def draw_rect(x, y, color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    for _ in range(4):
        turtle.forward(CELL_SIZE)
        turtle.left(90)
    turtle.end_fill()

# Function to draw the maze
def draw_maze(maze):
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == 1:  # Draw walls
                draw_rect(j * CELL_SIZE, -i * CELL_SIZE, "black")

# Recursive Backtracking algorithm to generate the maze
def generate_maze(maze, row, col):
    directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]  # Left, Right, Up, Down
    random.shuffle(directions)

    for d in directions:
        new_row = row + 2 * d[1]
        new_col = col + 2 * d[0]

        if 0 <= new_row < ROWS and 0 <= new_col < COLS and maze[new_row][new_col] == 0:
            maze[new_row - d[1]][new_col - d[0]] = 1
            maze[new_row][new_col] = 1
            generate_maze(maze, new_row, new_col)
    print(maze)

# Initialize screen
screen = turtle.Screen()
screen.setup(CELL_SIZE * COLS, CELL_SIZE * ROWS)
screen.setworldcoordinates(0, -CELL_SIZE * ROWS, CELL_SIZE * COLS, 0)
screen.tracer(0)

# Initialize Turtle
turtle.speed(0)
turtle.hideturtle()

# Create maze grid
maze = [[0] * COLS for _ in range(ROWS)]
maze[1][1] = 1  # Starting point
print(maze)
generate_maze(maze, 1, 1)

# Draw maze
draw_maze(maze)

# Update screen
screen.update()

# Keep the window open
turtle.done()
