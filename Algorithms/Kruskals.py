import turtle
import random


class DisjointSet:
    def __init__(self, n):
        # Initialize disjoint set with n elements, each element is its own parent
        self.parent = list(range(n))
        self.rank = [0] * n #creates a list of length n (for each vertex) where each element is initialized to 0

    def find(self, u):
        # Path compression heuristic
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        # Union by rank heuristic
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1


class Edge:
    def __init__(self, u, v, weight):
        self.u = u
        self.v = v
        self.weight = weight


def kruskal(n, edges):
    mst = []
    ds = DisjointSet(n)
    edges = sorted(edges, key=lambda edge: edge.weight)

    for edge in edges:
        if ds.find(edge.u) != ds.find(edge.v):
            ds.union(edge.u, edge.v)
            mst.append(edge)

    return mst


# Visualization with Turtle
def visualize_kruskal(n, edges, mst):
    # Screen setup
    screen = turtle.Screen()
    screen.title("Kruskal's Algorithm Visualization")
    screen.setup(width=800, height=600)

    # Turtle setup
    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()

    # Coordinates for vertices
    coords = [(random.randint(-300, 300), random.randint(-200, 200)) for _ in range(n)]

    # Draw vertices
    for i, (x, y) in enumerate(coords):
        t.penup()
        t.goto(x, y)
        t.dot(20, "black")
        t.write(f"{i}", align="center", font=("Arial", 12, "bold"))

    # Draw all edges
    for edge in edges:
        x1, y1 = coords[edge.u]
        x2, y2 = coords[edge.v]
        t.penup()
        t.goto(x1, y1)
        t.pendown()
        t.goto(x2, y2)
        t.penup()
        mx, my = (x1 + x2) / 2, (y1 + y2) / 2
        t.goto(mx, my)
        t.write(f"{edge.weight}", align="center", font=("Arial", 10, "normal"))

    # Highlight MST edges
    t.pensize(3)
    t.pencolor("red")
    for edge in mst:
        x1, y1 = coords[edge.u]
        x2, y2 = coords[edge.v]
        t.penup()
        t.goto(x1, y1)
        t.pendown()
        t.goto(x2, y2)

    screen.mainloop()


# Example usage:
edges = [
    Edge(0, 1, 10),
    Edge(0, 2, 6),
    Edge(0, 3, 5),
    Edge(1, 3, 15),
    Edge(2, 3, 4)
]
n = 4  # Number of vertices

mst = kruskal(n, edges)

print("Edges in the Minimum Spanning Tree:")
for edge in mst:
    print(f"{edge.u} -- {edge.v} == {edge.weight}")

# Visualize the result
visualize_kruskal(n, edges, mst)