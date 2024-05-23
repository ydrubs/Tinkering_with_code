import random

class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        # print(self.parent[u], '&&')
        return self.parent[u]

    def union(self, u, v):
        """If the walls do not have an opening, join them together.
        Reassigns u and v to the lower of the two values by checking which element (wall) has the lower rank."""
        # print('here')
        root_u = self.find(u)
        # print(root_u, '**')
        root_v = self.find(v)
        # print(root_u, root_v)
        ## self.parent[root_v] = root_u #Use the union by rank method instead below. This will result in a smaller parent list
        if root_u != root_v: #This line is prob. not necessary since the check is already done before union is called
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1

def create_maze(width, height):
    # Total cells in the maze
    n = width * height

    # Disjoint set for union-find
    ds = DisjointSet(n)

    # Generate all potential walls (edges)
    walls = []
    for x in range(width):
        for y in range(height):
            if x < width - 1:
                walls.append(((x, y), (x + 1, y)))
            if y < height - 1:
                walls.append(((x, y), (x, y + 1)))

    # Shuffle walls to ensure randomness
    print(walls)
    random.shuffle(walls)
    print(walls)

    # Maze structure (initially full of walls)
    maze = [[True for _ in range(2 * width + 1)] for _ in range(2 * height + 1)]
    for i in range(1, 2 * height, 2):
        for j in range(1, 2 * width, 2):
            maze[i][j] = False

    print(maze)


    # Kruskal's algorithm
    for (cell1, cell2) in walls:
        x1, y1 = cell1
        x2, y2 = cell2
        idx1 = y1 * width + x1
        idx2 = y2 * width + x2
        print(idx1,idx2, end='\n')

        """At first, each wall is independent, so the parent index of each will be unique, so the if-statement below runs.
           After every pass, when idx1 and idx2 are different, the parent index at each (idx1 and idx2) will be set equal to each other so they are not checked again.
           ...They are now part of the same set
           Then, the vert or hor wall is removed based on whether the x or y elements of each wall are the same. 
        """
        if ds.find(idx1) != ds.find(idx2): #Result of this check is whether the walls are part of the same set
            print('--', ds.parent[idx1], ds.parent[idx2])
            ds.union(idx1, idx2) #if not make them part of the same set
            # print('**', idx1,idx2)
            print('parent: ', ds.parent)
            print('rank: ', ds.rank)
            if x1 == x2:  # vertical wall
                maze[max(2 * y1, 2 * y2)][2 * x1 + 1] = False
            else:  # horizontal wall
                maze[2 * y1 + 1][max(2 * x1, 2 * x2)] = False
    print(len(set(ds.parent)))
    return maze

def print_maze(maze):
    for row in maze:
        print(''.join(['#' if cell else ' ' for cell in row]))

# Parameters for the maze
width = 3
height =3

# Create and print the maze
maze = create_maze(width, height)


# print_maze(maze)
