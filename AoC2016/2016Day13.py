
data = """1358"""
test = """10"""
testTarget = (7,4)
Target = (31,39)


import networkx as nx
def find_open(x,y , fav):
    ans = x*x + 3*x + 2*x*y + y + y*y
    ans += fav
    return bin(ans).count("1")%2==0
def solve(fav, target):
    fav = int(fav)
    grid = [[find_open(j, i, fav) for j in range(100)] for i in range(100)]
    G = nx.grid_2d_graph(100,100)
    for y in range(len(grid)):
        for x in range(len(grid)):
            if grid[y][x] == False:
                G.remove_node((x, y))
    print(nx.shortest_path_length(G, (1,1), target), "Part1")
    counter = 0
    for y in range(100):
        for x in range(100):
            if grid[y][x]:
                if nx.has_path(G, (1,1), (x, y)) and nx.shortest_path_length(G, (1,1), (x, y)) <= 50:
                    counter += 1
    print(counter, "Part2")
solve(test, testTarget)
solve(data, Target)