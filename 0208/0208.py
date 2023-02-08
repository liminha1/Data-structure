class Graph() :

    def __init__ (self, size) :
        self.SIZE = size
        self.graph = [ [0 for _ in range(size)] for _ in range(size)]

def printGraph(g) :
    print(' ', end=' ')
    for v in range(g.SIZE) :
        print(nameAry[v], end=' ')
    print()
    for row in range(g.SIZE) :
        print(nameAry[row], end=' ')
        for col in range(g.SIZE) :
            print(g.graph[row][col], end=' ')
        print()
    print()

G1 = None
nameAry = ['문문', '솔솔', '휘휘', '쯔쯔', '선선', '화화']
문문, 솔솔, 휘휘, 쯔쯔, 선선, 화화 = 0, 1, 2, 3, 4, 5

gSize = 6
G1 = Graph(gSize)
G1.graph[문문][솔솔] = 1; G1.graph[문문][휘휘] = 1
G1.graph[솔솔][문문] = 1; G1.graph[솔솔][쯔쯔] = 1
G1.graph[휘휘][문문] = 1; G1.graph[휘휘][쯔쯔] = 1
G1.graph[쯔쯔][솔솔] = 1; G1.graph[쯔쯔][휘휘] = 1; G1.graph[쯔쯔][선선] = 1
G1.graph[선선][쯔쯔] = 1; G1.graph[선선][화화] = 1
G1.graph[화화][쯔쯔] = 1; G1.graph[화화][선선] = 1

print('## G1 무방향 그래프 ##')
printGraph(G1 )


