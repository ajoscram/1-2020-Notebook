from math import sqrt

class Node:
    def __init__(self, name = "unknown", row = None, col = None):
        self.name = name
        self.row = row
        self.col = col
        self.enabled = True
        self.up = None
        self.right = None
        self.down = None
        self.left = None
    
    def toTuple(self):
        return ( self.row, self.col )

    def getEnabledNeighbors(self):
        neighbors = []
        if self.up and self.up.enabled:
            neighbors.append(self.up)
        if self.right and self.right.enabled:
            neighbors.append(self.right)
        if self.down and self.down.enabled:
            neighbors.append(self.down)
        if self.left and self.left.enabled:
            neighbors.append(self.left)
        return neighbors
    
    def getDistance(self, node):
        abscissa = self.col - node.col
        ordinate = self.row - node.row
        return sqrt( ordinate**2 + abscissa**2 )


class Labyrinth:
    def __init__(self, cast):
        row_number = len(cast)
        col_number = len(cast[0])
        self.grid = [[None for y in range(col_number)] for x in range(row_number)]
        for i in range(row_number):
            for j in range(col_number):
                if cast[i][j] > 0:
                    self.grid[i][j] = Node(chr(65+j)+str(i+1), i, j)
        for i in range(row_number):
            for j in range(col_number):
                if self.grid[i][j] != None:
                    if i > 0 and self.grid[i-1][j] != None:
                        self.grid[i][j].up = self.grid[i-1][j]
                    if i < row_number-1 and self.grid[i+1][j] != None:
                        self.grid[i][j].down = self.grid[i+1][j]
                    if j < col_number-1 and self.grid[i][j+1] != None:
                        self.grid[i][j].right = self.grid[i][j+1]
                    if j > 0 and self.grid[i][j-1] != None:
                        self.grid[i][j].left = self.grid[i][j-1]
    
    def reset(self, node):
        if node != None and node.enabled == False:
            node.enabled = True
            self.reset(node.up)
            self.reset(node.right)
            self.reset(node.down)
            self.reset(node.left)

    def search(self, start, end, algorithm):
        startNode = self.grid[start[0]][start[1]]
        endNode = self.grid[end[0]][end[1]]
        stats = Stats(start, end)
        algorithm(startNode, endNode, stats)
        self.reset(startNode)
        return stats
    
    def print(self):
        result = ''
        for row in self.grid:
            for node in row:
                if node == None:
                    result += '■\t'
                else:
                    result += node.name + '\t'
            result += '\n'
        print(result)

    def draw(self, path):
        return None

class Stats:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.steps = 0
        self.solved = False
        self.visited = []

    @property
    def cost(self):
        return len(self.visited)
    
    def __str__(self):
        result =  "Start:\t\t"+str(self.start)+"\n"
        result += "End:\t\t"+str(self.end)+"\n"
        result += "Steps:\t\t"+str(self.steps)+"\n"
        result += "Cost:\t\t"+str(self.cost)+"\n"
        result += "Solved:\t\t"+str(self.solved)
        return result

#-------------------------------------------------------------------------------------------------------------

def depthSearch(current, target, stats):
    stats.visited += [current.toTuple()]
    stats.steps += 1
    current.enabled = False
    if current == target:
        stats.solved = True
        return [current]
    for neighbor in current.getEnabledNeighbors():
        result = depthSearch(neighbor, target, stats)
        if result != []:
            return [current] + result
    return [ ]

def breadthSearch(current, target, stats):
    nodes = [current]
    visited = []
    while nodes != []:
        stats.steps += 1
        newNodes = []
        for node in nodes:
            node.enabled = False
            visited += [node]
            stats.visited += [node.toTuple()]
            if node == target:
                stats.solved = True
                return visited
            newNodes += node.getEnabledNeighbors()
        nodes = newNodes
    stats.solved = False
    return visited

def hillClimbingSearch(current, target, stats):
    stats.visited += [current.toTuple()]
    stats.steps += 1
    current.enabled = False
    neighbors = current.getEnabledNeighbors()
    if current == target:
        stats.solved = True
        return [current]
    elif neighbors == []:
        stats.solved = False
        return [current]
    else:
        best = neighbors[0]
        for neighbor in neighbors:
            if neighbor.getDistance(target) < best.getDistance(target):
                best = neighbor
        return [current] + hillClimbingSearch(best, target, stats)

#--------------------------------------------------------------------------------------------------------------

cast = [
  [0,1,1,1,0,1,1,1,0,1],
  [0,0,1,0,0,1,0,0,0,1],
  [0,1,1,1,1,1,1,1,1,1],
  [0,0,0,0,0,1,0,0,0,0],
  [1,1,1,0,1,1,1,1,1,1],
  [1,0,0,0,1,0,0,0,1,0],
  [1,1,1,1,1,0,1,0,1,1],
  [0,0,0,0,1,0,1,0,1,0],
  [1,1,1,1,1,1,1,0,1,1]
]

lab = Labyrinth(cast)
lab.print()
print(lab.search((8,4), (0, 7), depthSearch))
print('------------------------------------')
print(lab.search((8,4), (0, 7), breadthSearch))
print('------------------------------------')
print(lab.search((8,4), (0, 7), hillClimbingSearch))
print('------------------------------------')
print(lab.search((0,1), (0, 7), hillClimbingSearch))