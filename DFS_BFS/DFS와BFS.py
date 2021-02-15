# 삼성 SW 역량테스트에서는 sys 모듈 일부 제한 있음
# DFS의 장점 : 한 경로상의 노드를 기억하기 때문에 적은 메모리 사용, 찾으려는 노드가 깊은 단계인 경우 BFS보다 빠르다
# DFS의 단점 : 해가 없는 경로를 탐색할 경우 단계가 끝날 때까지 탐색한다. DFS는 해에 도착하면 탐색을 종료하기 때문에 최단경로라는 보장이 없다


from sys import stdin
n, m, v = map(int, stdin.readline().split())
matrix = [[0] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    line = list(map(int, stdin.readline().split()))
    matrix[line[0]][line[1]] = 1
    matrix[line[1]][line[0]] = 1

def bfs(start):
    visited=[start]
    queue=[start]
    while queue:
        n=queue.pop(0)
        for c in range(len(matrix[start])):
            if matrix[n][c]==1 and (c not in visited):
                visited.append(c)
                queue.append(c)
    return visited
def dfs(start, visited):
    visited+=[start]
    for c in range(len(matrix[start])):
        if matrix[start][c]==1 and (c not in visited):
            dfs(c, visited)
    return visited        

print(*dfs(v, []))
print(*bfs(v))