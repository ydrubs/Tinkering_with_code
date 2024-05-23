"""
Holds the data structure for creating and transversing through a maze.
The following methods are used:
    - create_maze_data(rows, columns) - Takes the number of rows and columns desired and returns the data for walls and passages in the grid.
        All passages are represented by a 0 and all walls represented by a 1.
    - corners(array) - takes the data for the grid and changes the four corner walls to 'x' - helps with debugging and visualization.
    - make_passage(array, direction, row, col) - Takes in the maze data, the desired direction to create an opening by removing a wall
            (up, left, down, right), and the row/column from which to create the opening.
            Does not return anything but acts on the maze data created by the create_maze_data method.
    - get_accessible_neighbors(maze, row, col) - takes the grid data and a row/col and returns which neighbor cells are accessible as a list.
"""

from math import ceil

def create_maze_data(rows, columns):
    """Take in number of rows and columns and return the data structure representing walls and openings"""
    array = [[1 for i in range((columns*2)+1)] for j in range((rows*2)+1)] #Initially everything is a wall
    for i in range(1, len(array),2): #..Then create openings to represent cell locations
        # print(walls_and_passages[i])
        for j in range(1,len(array[i]),2):
           array[i][j] = 0
    return array


def corners(array):
    """Make 4 corners of maze as 'x' in data"""
    last_col = len(array[0])
    last_row = len(array)
    array[0][0] = 'x'
    array[0][last_col-1] = 'x'
    array[last_row-1][0] = 'x'
    array[last_row-1][last_col-1] = 'x'
    return array


def make_passage(array, direction, row, col):
    """Create passageways by removing walls in the data structure (replace 1 with 0)"""
    #Start at current cell
    #change a 1 to a zero depending on where the wall is relative to current cell
    ##Example with cell at row 2, column 2 or  (1,1) in array structure
    ##Define location relative to row and column
    walls_and_passages = array
    row = 2*row + 1
    col = 2*col + 1
    # current_cell = '#'
    # walls_and_passages[row][col] = current_cell
    dir = ((row-1), (row+1), (col+1), (col-1)) #top, bottom, right, left
    # current_cell = walls_and_passages[row][col]

    if direction == 'up':
    #Remove top wall
        walls_and_passages[dir[0]][col] = 0
    if direction == 'left':
    #remove left wall
        walls_and_passages[row][dir[3]] = 0
    if direction == 'down':
    #Remove bottom wall
        walls_and_passages[dir[1]][col] = 0
    #Remove right wall
    if direction == 'right':
        walls_and_passages[row][dir[2]] = 0

def get_accessible_neighbors(maze, row, col):
    row = 2*row + 1
    col = 2*col + 1
    dir = ((row-1), (row+1), (col+1), (col-1)) #top, bottom, right, left
    accessible_neighbors = []
    # print(maze)

    if maze[dir[0]][col] == 0: #Top is accessible
        accessible_neighbors.append((ceil((dir[0] - 2) / 2), ceil((col - 1) / 2)))

    if maze[row][dir[3]] == 0: #Left is accessible
        accessible_neighbors.append((ceil((row - 1) / 2), ceil((dir[3] - 2) / 2)))

    if maze[dir[1]][col] == 0: #Bottom is accessible
        accessible_neighbors.append((ceil((dir[1] - 1) / 2), ceil((col - 1) / 2)))

    if maze[row][dir[2]] == 0: #Right is accssible
        accessible_neighbors.append((ceil((row - 1) / 2), ceil((dir[2] - 1) / 2)))

    accessible_neighbors = [n for n in accessible_neighbors if n[0] > -1 and n[1] > -1]

    return accessible_neighbors


if __name__ == '__main__':
    # grid = grid_template.grid(4,4, cell_dim=60, border=61)
    # grid.build_grid()
    # walls_and_passages = [[1 for i in range((grid.columns*2)+1)] for j in range((grid.rows*2)+1)]
    maze_data = create_maze_data(6,6)
    make_passage(maze_data, 'up', 4,2) #Expect 3,2 when input of 4,2
    make_passage(maze_data, 'left', 4,2) #Expect 4, 1
    # make_passage(maze_data, 'down', 0,0) #Expect 5,2
    # make_passage(maze_data, 'right', 0,0) #Expect 4,3

    # for i in maze_data:
        # print(i)
    # maze_data[1][1] = 2
    # print(get_accessible_neighbors(maze_data,4,2))

