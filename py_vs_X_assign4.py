"""
<INSERT YOUR NAME HERE>
"""

# for timing checks
import time


def adjMatFromFile(filename):
    """ Create an adj/weight matrix from a file with verts, neighbors, and weights. """
    f = open(filename, "r")
    n_verts = int(f.readline())
    print(f" n_verts = {n_verts}")
    adjmat = [[None] * n_verts for i in range(n_verts)]
    for i in range(n_verts):
        adjmat[i][i] = 0
    for line in f:
        int_list = [int(i) for i in line.split()]
        vert = int_list.pop(0)
        assert len(int_list) % 2 == 0
        n_neighbors = len(int_list) // 2
        neighbors = [int_list[n] for n in range(0, len(int_list), 2)]
        distances = [int_list[d] for d in range(1, len(int_list), 2)]
        for i in range(n_neighbors):
            adjmat[vert][neighbors[i]] = distances[i]
    f.close()
    return adjmat


def prim(W):
    F = []

    # IF YOU HAVE CHOSEN PRIM'S, THEN COPY AND PASTE YOUR ASSIGN 4 CODE HERE

    return F


def kruskal(W):
    F = []

    # IF YOU HAVE CHOSEN KRUSKAL'S, THEN COPY AND PASTE YOUR ASSIGN 4 CODE HERE

    return F


def assign04_main():
    """ Demonstrate the functions, starting with creating the graph. """
    g = adjMatFromFile("py_vs_X_assign4.txt")

    # Run Prim's algorithm
    start_time = time.time()
    res_prim = prim(g)
    elapsed_time_prim = time.time() - start_time
    print(f"Prim's runtime: {elapsed_time_prim:.6f}")

    # Run Kruskal's for a single starting vertex, 2
    start_time = time.time()
    res_kruskal = kruskal(g)
    elapsed_time_kruskal = time.time() - start_time
    print(f"Kruskal's runtime: {elapsed_time_kruskal:.6f}")

    # If above assert passed, then it doesn't matter which result is used
    cost_prim = sum([e[2] for e in res_prim])
    cost_kruskal = sum([e[2] for e in res_kruskal])
    assert cost_prim == cost_kruskal
    print("MST cost prim: ", cost_prim)
    print("MST cost kruskal: ", cost_kruskal)


# Check if the program is being run directly (i.e. not being imported)
if __name__ == '__main__':
    assign04_main()
