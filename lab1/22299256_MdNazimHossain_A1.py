import heapq


# Task -1
def task01(inputFileName):
    fileName = inputFileName
    output = open("output_part1.txt", 'w')

    maze = []

    with open(fileName, "r") as f:
        height, width = map(int, f.readline().strip().split(", "))
        start_row, start_col = map(int, f.readline().strip().split(", "))
        goal_row, goal_col = map(int, f.readline().strip().split(", "))

        for _ in range(height):
            maze.append(list(f.readline().strip().replace(" ","")))

    # for i in maze:
    #     print(i)
    start_pos = (start_row, start_col)
    goal_pos = (goal_row, goal_col)
    queue = []
    visited = set()
    parent_of = {}

    def h(curr_pos):
        return abs(curr_pos[0]-goal_pos[0]) + abs(curr_pos[1] - goal_pos[1])

    curr_pos = start_pos

    curr_g = 0
    curr_f = curr_g + h(curr_pos)
    
    heapq.heappush(queue, (curr_f, curr_g, curr_pos))

    goal_found = False
    while queue:
        curr_f , curr_g, curr_pos= heapq.heappop(queue)

        if curr_pos == goal_pos:
            goal_found = True
            
            path = []
            i = curr_pos
            # print("gaol: ", type(i), "start: ", type(start_pos))
            while i != start_pos:
                parent = parent_of[i]

                if parent[0] + 1 == i[0]:
                    path.append("down")
                elif parent[0] - 1 == i[0]:
                    path.append("up")
                elif parent[1] + 1 == i[1]:
                    path.append("right")
                elif parent[1] - 1 == i[1]:
                    path.append("left")

                i = parent
            path.reverse()
            print(*path, sep="-->", file=output)
            print("Total steps: ", curr_g, file=output)
            break
        if curr_pos in visited:
            continue
        visited.add(curr_pos)

        if ((curr_pos[0]+1) < height) and maze[curr_pos[0]+1][curr_pos[1]] == '0':
            new_pos = (curr_pos[0]+1, curr_pos[1])
            if new_pos not in visited:
                new_g = curr_g + 1
                new_f = new_g + h(new_pos)
                parent_of[new_pos] = curr_pos
                heapq.heappush(queue, (new_f, new_g, new_pos))
        if ((curr_pos[1] + 1) < width) and maze[curr_pos[0]][curr_pos[1]+1] == "0":
            new_pos = (curr_pos[0], curr_pos[1]+1)
            if new_pos not in visited:
                new_g = curr_g + 1
                new_f = new_g + h(new_pos)
                parent_of[new_pos] = curr_pos
                heapq.heappush(queue, (new_f, new_g, new_pos))
        if ((curr_pos[0] - 1) >= 0) and maze[curr_pos[0]-1][curr_pos[1]] == '0':
            new_pos = (curr_pos[0]-1, curr_pos[1])
            if new_pos not in visited:
                new_g = curr_g + 1
                new_f = new_g + h(new_pos)
                parent_of[new_pos] = curr_pos
                heapq.heappush(queue, (new_f, new_g, new_pos))
        if ((curr_pos[1] - 1) >= 0) and maze[curr_pos[0]][curr_pos[1] - 1] == "0":
            new_pos = (curr_pos[0], curr_pos[1]-1)
            if new_pos not in visited:
                new_g = curr_g + 1
                new_f = new_g + h(new_pos)
                parent_of[new_pos] = curr_pos
                heapq.heappush(queue, (new_f, new_g, new_pos))

    if(goal_found == False):
        print("No path found", file=output)

task01("input_part1_3.txt") #Enter the input file/path part 1
# <----- Uncomment the line above to run task01 ------>

# task 2
from collections import deque

def task02(inputFile):
    filename = inputFile
    output= open("output_part2.txt", "w")
    h = {} #Heruistic
    graph = {} #Adj list

    with open(filename, "r") as f:
        numVertices, numEdges = map(int, f.readline().strip().split(" "))
        start, goal = map(int, f.readline().strip().split(" "))
        for i in range(1, numVertices+1):
            x, y = map(int, f.readline().strip().split(" "))
            h[x] = y
            graph[i] = []
        for _ in range(numEdges):
            u, v = map(int, f.readline().strip().split(" "))
            graph[u].append(v)
            graph[v].append(u)

    # print(h)
    # print(graph)

    def bfs(graph, source, numVertices):
        dis = {}
        for i in range(1, numVertices + 1):
            dis[i] = float('inf')
        
        dis[source] = 0

        dq = deque([source])

        while dq:

            curr_v = dq.popleft()

            for n in graph[curr_v]:
                if dis[n] == float('inf'):
                    dis[n] = dis[curr_v] + 1
                    dq.append(n)
        return dis


    actual = bfs(graph, goal, numVertices)

    items = []

    for i in range(1, numVertices + 1):
        if h[i] > actual[i]:
            items.append(i)

    if len(items) > 1:
        res = "Here nodes "
        for i in range(len(items) -1):
            res+= str(items[i]) + ","

        res += "and " + str(items[-1]) + " are inadmissible."
        print(res, file=output)
    elif len(items) == 1:
        print(f"Here node {items[0]} is inadmissible.")
    else:
        print("The heuristic values are admissible.", file=output)

task02("input_part2_1.txt") #Enter the input file/path for part2






