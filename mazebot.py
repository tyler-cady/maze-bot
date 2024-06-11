import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 500, 500
ROWS, COLS = 50, 50
CELL_SIZE = WIDTH // COLS

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Create the display
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maze Solver")

# Generate the maze using depth-first search (DFS)
def generate_maze(rows, cols):
    maze = [[1 for _ in range(cols)] for _ in range(rows)]
    stack = []
    start = (random.randint(0, rows-1), random.randint(0, cols-1))
    stack.append(start)
    maze[start[0]][start[1]] = 0

    while stack:
        current = stack[-1]
        neighbors = []
        directions = [(-2, 0), (2, 0), (0, -2), (0, 2)]

        for direction in directions:
            nx, ny = current[0] + direction[0], current[1] + direction[1]
            if 0 <= nx < rows and 0 <= ny < cols and maze[nx][ny] == 1:
                neighbors.append((nx, ny))

        if neighbors:
            next_cell = random.choice(neighbors)
            stack.append(next_cell)
            maze[next_cell[0]][next_cell[1]] = 0
            in_between_x = (current[0] + next_cell[0]) // 2
            in_between_y = (current[1] + next_cell[1]) // 2
            maze[in_between_x][in_between_y] = 0
        else:
            stack.pop()

    return maze, start

# Ensure the end point is not directly vertical or horizontal to the start point
def get_valid_end(start, rows, cols):
    while True:
        end = (random.randint(0, rows-1), random.randint(0, cols-1))
        if end[0] != start[0] and end[1] != start[1]:
            return end

# Draw the maze with outlined paths
def draw_maze(win, maze):
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == 0:  # Only draw paths
                pygame.draw.rect(win, WHITE, (j * CELL_SIZE, i * CELL_SIZE, CELL_SIZE, CELL_SIZE))
                pygame.draw.rect(win, BLACK, (j * CELL_SIZE, i * CELL_SIZE, CELL_SIZE, CELL_SIZE), 1)

# Dot class
class Dot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, win):
        pygame.draw.circle(win, RED, (self.x * CELL_SIZE + CELL_SIZE // 2, self.y * CELL_SIZE + CELL_SIZE // 2), CELL_SIZE // 4)

    def move(self, dx, dy):
        new_x = self.x + dx
        new_y = self.y + dy
        if 0 <= new_x < COLS and 0 <= new_y < ROWS and maze[new_y][new_x] == 0:
            self.x = new_x
            self.y = new_y

# Function to check if dot is on the blue square
def isBlue(dot):
    dot_center_x = dot.x * CELL_SIZE + CELL_SIZE // 2
    dot_center_y = dot.y * CELL_SIZE + CELL_SIZE // 2
    blue_square_x = finish_x * CELL_SIZE
    blue_square_y = finish_y * CELL_SIZE
    return (blue_square_x <= dot_center_x < blue_square_x + CELL_SIZE) and (blue_square_y <= dot_center_y < blue_square_y + CELL_SIZE)

# Function to get possible moves
def getPossibleMoves(dot):
    possible_moves = []
    if dot.y > 0 and maze[dot.y - 1][dot.x] == 0:  # Up
        possible_moves.append((0, -1))
    if dot.y < ROWS - 1 and maze[dot.y + 1][dot.x] == 0:  # Down
        possible_moves.append((0, 1))
    if dot.x > 0 and maze[dot.y][dot.x - 1] == 0:  # Left
        possible_moves.append((-1, 0))
    if dot.x < COLS - 1 and maze[dot.y][dot.x + 1] == 0:  # Right
        possible_moves.append((1, 0))
    return possible_moves

# Functions to control the dot
def up():
    dot.move(0, -1)

def down():
    dot.move(0, 1)

def left():
    dot.move(-1, 0)

def right():
    dot.move(1, 0)

def bot_solve(dot):
    # Stack of moves
    stack = []

    while not isBlue(dot):
        possibleMoves = getPossibleMoves(dot)
        if len(possibleMoves) == 0:
            break
        # Search assuming you can't see anything but available moves and only can know if a square is blue when you are on it
        if len(possibleMoves) > 1:
            # Choose Forward, Left, Right, Back in that order
            if (0, -1) in possibleMoves:
                stack.append((0, -1))
                up()
            elif (-1, 0) in possibleMoves:
                stack.append((-1, 0))
                left()
            elif (1, 0) in possibleMoves:
                stack.append((1, 0))
                right()
            elif (0, 1) in possibleMoves:
                stack.append((0, 1))
                down()
        else:
            # If the move is back then pop the last move from the stack
            if len(stack) > 0:
                last_move = stack.pop()
                dx, dy = last_move
                dot.move(-dx, -dy)
            else: # If the move is forward then move forward add moves to stack
                dx, dy = possibleMoves[0]
                stack.append((dx, dy))
                dot.move(dx, dy)
    return stack

def solve_from_stack(stack, is_backtrack):
    if is_backtrack:
        dx, dy = stack[-1]
        stack.pop()
        dot.move(-dx, -dy)
    else:
        dx, dy = stack[-1]
        stack.pop()
        dot.move(dx, dy)

# Main loop
maze, start = generate_maze(ROWS, COLS)
finish_x, finish_y = get_valid_end(start, ROWS, COLS)
maze[finish_y][finish_x] = 0
dot = Dot(start[1], start[0])

running = True
solved = False
bot_started = False
# Inside the while loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:  # Check if spacebar is pressed
                bot_started = True  # Set flag to indicate bot has started
            if not solved and bot_started:  # Only start bot if it hasn't been solved and bot_started is True
                stack = bot_solve(dot)
                bot_started = False  # Reset the flag after the bot has finished solving
            else:
                while True:
                    print("Maze solved!")
                    solve_from_stack(stack, True)
                    solve_from_stack(stack, False)
    # Move the dot and update the display
    win.fill(BLACK)
    draw_maze(win, maze)
    pygame.draw.rect(win, BLUE, (finish_x * CELL_SIZE, finish_y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
    dot.draw(win)
    pygame.display.update()  # Update the display after each iteration of the while loop


pygame.quit()
