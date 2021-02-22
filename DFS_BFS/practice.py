from collections import deque
import sys

N, M = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

q = deque()
for i in range(M):
	for j in range(N):
		if graph[i][j] == 1:
			q.append([i, j])

while q:
	x, y = q.popleft()

	for i in range(4):
		xx = dx[i] + x
		yy = dy[i] + y	

		if M > xx >= 0 and N > yy >= 0:
			if graph[xx][yy] == 0:
				graph[xx][yy] = 1
				graph[xx][yy] = graph[x][y] + 1
				q.append([xx, yy])

result = -2
check_graph = False

for i in graph:
	for j in i:
		if j == 0:
			check_graph = True
		result = max(result, j)
if check_graph:
	print(-1)
elif result == -1:
	print(0)
else:
	print(result - 1)