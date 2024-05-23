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