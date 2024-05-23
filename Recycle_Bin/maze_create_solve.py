import time
from icecream import ic
import turtle as t
from itertools import cycle
import random
from collections import deque
from Grid_Building import grid_template
from Recycle_Bin import maze_data_structure
from Algorithms import Union_Find_Kruskals


def remove_wall(dir, row, col):
    t.pensize(4)
    t.color(grid.bg_color)
    row, col = row+1, col+1

    # t.tracer(1)

    ##Bottom wall of a cell remove
    if dir == 'down':
        t.up()
        remove_wall = grid.get_cell_boundaries_single(row, col)
        t.goto(remove_wall[0]+grid.line_thickness_hor+1, remove_wall[3])
        t.down()
        t.goto(remove_wall[1]-grid.line_thickness_hor-1, remove_wall[3])
        ##Update the array holding the passage data
        maze_data_structure.make_passage(walls_and_passage_data, dir, row - 1, col - 1)
        t.update()

    # Top wall remove
    if dir == 'up':
        t.up()
        t.color(grid.bg_color)
        remove_wall = grid.get_cell_boundaries_single(row, col)
        t.goto(remove_wall[0]+grid.line_thickness_hor+1, remove_wall[2])
        t.down()
        t.goto(remove_wall[1]-grid.line_thickness_hor-1, remove_wall[2])
        maze_data_structure.make_passage(walls_and_passage_data, dir, row - 1, col - 1)
        t.update()

    #Left Wall Remove
    if dir == 'left':
        t.up()
        t.color(grid.bg_color)
        remove_wall = grid.get_cell_boundaries_single(row, col)
        t.goto(remove_wall[0], remove_wall[2]-2)
        t.down()
        t.goto(remove_wall[0], remove_wall[3]+2)
        maze_data_structure.make_passage(walls_and_passage_data, dir, row - 1, col - 1)
        t.update()

    if dir == 'right':
        #Right wall Remove
        t.up()
        t.color(grid.bg_color)
        remove_wall = grid.get_cell_boundaries_single(row, col)
        t.goto(remove_wall[1], remove_wall[2]-grid.line_thickness_hor-1)
        t.down()
        t.goto(remove_wall[1], remove_wall[3]+grid.line_thickness_hor+1)
        maze_data_structure.make_passage(walls_and_passage_data, dir, row - 1, col - 1)
        t.update()

def generate_maze(row, col):
    """Use a randomized Mazes to generate a maze """
    ###Start at 0,0
    ###Get all the possible neighbors
    ###Choose a random neighbor
    ###Remove the wall between them if there is one
    ###Go on to the next neigbor and do the same

    walls_removed = {}

    #Create a start and end position opening
    remove_wall('up', row, col)
    maze_data_structure.make_passage(walls_and_passage_data, 'up', row, col)
    remove_wall('left', grid.rows-1, grid.columns-1)
    maze_data_structure.make_passage(walls_and_passage_data, 'left', grid.rows - 1, grid.columns - 1)
    remove_wall('down', grid.rows-1, grid.columns-1)
    maze_data_structure.make_passage(walls_and_passage_data, 'down', grid.rows - 1, grid.columns - 1)

    #set the start position
    grid.grid_array_data[row][col] = 1

    #Set the end position
    end_row, end_col = grid.rows-1, grid.columns-1
    grid.grid_array_data[end_row][end_col] = 1
    # ic(grid.grid_array_data)

    # Create a stack to keep track of visited cells
    stack = [(row, col)]

    # Generate the maze using Depth-First Search algorithm
    while stack:
    # for i in range(200):
        current_row, current_col = stack[-1]
        # print(stack, current_row)

        # Find all neighbors of current cell
        neighborhood = []
        neighbors = grid.get_neighbors(current_row, current_col)
        # ic(neighbors)
        # ic(grid.grid_array_data)

        # Only keep unvisitied neighbors
        for n in neighbors:
            if grid.grid_array_data[n[0]][n[1]] == 0:
                neighborhood.append(n)

        if neighborhood:
            # Choose a random neighbor
            chosen_neighbor = random.choice(neighborhood)
            # ic(chosen_neighbor)
            #Remov the wall between current cell and chosen neighbor
            remove_wall(chosen_neighbor[2], current_row, current_col)
            walls_removed[current_row, current_col] = chosen_neighbor[2]

            # Mark the chosen neighbor as visited
            grid.grid_array_data[chosen_neighbor[0]][chosen_neighbor[1]] = 1

            # Add the chosen neighbor to the stack
            stack.append((chosen_neighbor[0], chosen_neighbor[1]))

        else:
            # Backtrack if there are no unvisited neighbors
            stack.pop()

def create_kruskals(maze_data):
    # Total cells in the maze
    n = grid.rows * grid.columns

    # Disjoint set for union-find
    ds = Union_Find_Kruskals.DisjointSet(n)
    # print(maze_data)

    cell_data = grid.get_connections_all()
    random.shuffle(cell_data)
    # print(cell_data)

    ##Break out into its own function for the start and end set
    #Create a start and end position opening
    remove_wall('up', 0, 0)
    maze_data_structure.make_passage(walls_and_passage_data, 'up', 0, 0)
    remove_wall('left', grid.rows-1, grid.columns-1)
    maze_data_structure.make_passage(walls_and_passage_data, 'left', grid.rows - 1, grid.columns - 1)
    remove_wall('down', grid.rows-1, grid.columns-1)
    maze_data_structure.make_passage(walls_and_passage_data, 'down', grid.rows - 1, grid.columns - 1)

    # Kruskal's algorithm
    for (cell1, cell2) in cell_data:
        x1, y1 = cell1
        x2, y2 = cell2
        idx1 = y1 * grid.columns + x1
        idx2 = y2 * grid.columns + x2
        # print(idx1,idx2, end='\n')

        if ds.find(idx1) != ds.find(idx2):  # Result of this check is whether the walls are part of the same set
            # print('--', ds.parent[idx1], ds.parent[idx2])
            ds.union(idx1, idx2)  # if not make them part of the same set
            # print('**', idx1,idx2)
            # print('parent: ', ds.parent)
            # print('rank: ', ds.rank)
            if x1 == x2:  # vertical wall
                maze_data[max(2 * y1, 2 * y2)][2 * x1 + 1] = 0
            else:  # horizontal wall
                maze_data[2 * y1 + 1][max(2 * x1, 2 * x2)] = 0

    # print(sorted(cell_data))
    # print(maze_data[1][2], maze_data[1][4])

    for x, i in enumerate(maze_data):
        if x%2 == 1:
            # print(i)
            for y, j in enumerate(i):
                if y%2 ==0:
                    # print(j)
                    if j == 0:
                        remove_wall('right', (x-1)//2, (y-1)//2)
            if x >= 3:
                # print(i, '***')
                for z, k in enumerate(i):
                    if z%2 == 1:
                        if maze_data[x-1][z] == 0:
                            # print('here', x-1, z)
                            # remove_wall('up', x-1, z)
                            remove_wall('up', ((x-1)//2), (z-1)//2)

    ##Go to row 2 and explore it
    ##If the cell directly above the cell in row to is a '0', remove the floor


    # print(len(set(ds.parent)))


    # remove_wall('up' , 2,1)

    return maze_data


def solve_DFS(maze_data):
    t.color('black')
    t.up()
    step_count = 0
    colors = cycle(['red', 'green', 'blue', 'LightSalmon2'])

    ##start at cell (0,0)
    row, col = 0,0
    t.goto(grid.grid_data_centers()[row][col][0], grid.grid_data_centers()[row][col][1])
    t.down()

    #Set up data to hold visited cells and the cells that are needed to be visites as well as a rule for stopping the maze search
    goal = (grid.rows-1, grid.columns-1)
    visited = [(0,0)]
    need_to_visit=[(0,0)]

    while need_to_visit:
        step_count+=1
        if goal in visited:
            print(f"Exit Found! in {step_count} moves")
            break

        row, col = need_to_visit.pop()
        # print('here')
        ##Get the accessible neighbor(s) of the current cell if they have not been visited yet
        accessible_neighbors = maze_data_structure.get_accessible_neighbors(maze_data, row, col)
        accessible_neighbors = [n for n in accessible_neighbors if n not in visited]
        # print(accessible_neighbors)

        #If there are any accessible neighbors that have not been visited, draw a line to the next neighbor and mark it as visited
        if accessible_neighbors and accessible_neighbors[-1] not in visited:
            next_row, next_col = accessible_neighbors.pop()
            visited.append((next_row, next_col))
            t.goto(grid.grid_data_centers()[next_row][next_col][0], grid.grid_data_centers()[next_row][next_col][1])

            #If there is another neighbor (or more) to visit, we have multiple paths, add it to the need_to_visit list
            if accessible_neighbors:
                for _ in accessible_neighbors: #In the case where there is more then two paths, make sure to add ALL neighbors
                    need_to_visit.append(_)

        else: #if no accessible neighbors backtrack and take the last location on the need_to_visit list
            if need_to_visit: #...as long as there is a cell that can be visited
                # t.up()
                next_row, next_col = need_to_visit.pop()
                # t.color('red')
                t.color(next(colors))
                visited.append((next_row, next_col))
                t.pensize(1)
                t.goto(grid.grid_data_centers()[next_row][next_col][0], grid.grid_data_centers()[next_row][next_col][1])
                t.pensize(4)
                t.down()
            else:
                break

        #Make the next row equal to the current row for the next iteration
        # row, col = next_row, next_col
        need_to_visit.append((next_row, next_col))
        # print(need_to_visit, '%%')
        t.update()

def solve_BFS(maze_data):
    """Uses a BFS algorithm to search through a maze. The process is:
        1) Remove a cell from the beginning of the queue
        2) Visit the neighbors if they have not been visited yet and add them to the end of the queue
        3) add the neighbors to the visited set
        4) Add the path to the neignbors from the current cell as a key:value pair
        """
    t.color('black')
    t.up()

    ##start and end positions
    row, col = 0,0
    start = (row,col)
    end = (grid.rows-1, grid.columns-1)
    t.goto(grid.grid_data_centers()[row][col][0], grid.grid_data_centers()[row][col][1]) #Place pen at the start position
    # t.down()

    # Create a queue for BFS and a set to keep track of visited nodes
    queue = deque([start])
    visited = set([start])
    path = {start: None} #Use to keep track of path and retrace steps of solution
    # print(visited)

    while queue:

        # Dequeue a cell from the queue and set it as current cell
        current_cell = queue.popleft()
        row, col = current_cell[0], current_cell[1]
        # print(row, col)

        #Draw the path
        t.goto(grid.grid_data_centers()[row][col][0], grid.grid_data_centers()[row][col][1])
        t.dot(5, 'red')

        # Explore neighbors
        accessible_neighbors = maze_data_structure.get_accessible_neighbors(maze_data, row, col)
        accessible_neighbors = [n for n in accessible_neighbors if n not in visited]
        # print(accessible_neighbors)

        # If there is another neighbor (or more) to visit, we have multiple paths, add it to the need_to_visit list
        if accessible_neighbors:
            for _ in accessible_neighbors:  # In the case where there is more then two paths, make sure to add ALL neighbors
                queue.append(_)
                visited.add(_)
                path[_] = current_cell
                # print(path)


        # If we reach the end, reconstruct the path
        if current_cell == end:
            #Place a dot to mark end location
            t.goto(grid.grid_data_centers()[end[0]][end[1]][0], grid.grid_data_centers()[end[0]][end[1]][1])
            t.dot(7, 'blue')
            shortest_path = [] #Build the shortest path from start to finish
            #Grab the neigbor cell leading from the current cell in the path dictionary (as long as the path exists)
            while current_cell:
                shortest_path.append(current_cell)
                current_cell = path[current_cell]
            shortest_path.reverse() #reverse the path to go from start to finish
            # print(shortest_path, '**')

            #Draw the shortest path
            t.goto(grid.grid_data_centers()[start[0]][start[1]][0], grid.grid_data_centers()[start[0]][start[1]][1])
            time.sleep(0.5)
            for move in shortest_path:
                trace_row, trace_col = move[0], move[1]
                # print(trace_row, trace_col)
                t.down()
                t.goto(grid.grid_data_centers()[trace_row][trace_col][0], grid.grid_data_centers()[trace_row][trace_col][1])
                t.update()
            return None

        # time.sleep(0.1)
        t.update()
    # return None

def next_step_shade():
    #Start by making a deep copy of the states of the current iteration in order to use for next iteration
    t.color('purple')
    # grid.grid_array_data = copy.deepcopy(grid.next_step_array)
    cell_border = 0
    for x, row in enumerate (grid.grid_array_data):
        for y, cell in enumerate (row):
            if cell == 1:
                # print(cell, '#@!')
                # print(next_step_array, x,y)
                selected_cell = grid.get_cell_boundaries_single(x+1, y+1)
                # print(selected_cell)
                t.goto(selected_cell[0]+cell_border, selected_cell[2]-cell_border)
                t.begin_fill()
                t.goto(selected_cell[0]+cell_border, selected_cell[3]+cell_border)
                t.goto(selected_cell[1]-cell_border, selected_cell[3]+cell_border)
                t.goto(selected_cell[1]-cell_border, selected_cell[2]-cell_border)
                t.end_fill()
    t.update()

if __name__ == '__main__':
    ic.configureOutput(includeContext=True)
    grid = grid_template.grid(50, 50, cell_dim=10, border=40)
    grid.build_grid()
    grid.grid_data_centers()
    walls_and_passage_data = maze_data_structure.create_maze_data(grid.rows, grid.columns)

    # print(walls_and_passage_data)
    # print(grid.grid_data_centers())
    # print(grid.grid_array_data)


    # print('\n\n', walls_and_passage_data)
    # print(grid.grid_data_centers())
    # print(grid.grid_array_data, 'h')
    # generate_maze(0,0)
    # solve_DFS(walls_and_passage_data)
    # solve_BFS(walls_and_passage_data)
    k_maze = create_kruskals(walls_and_passage_data)
    # solve_DFS(k_maze)
    solve_BFS(k_maze)
    # print(k_maze)
    t.done()

