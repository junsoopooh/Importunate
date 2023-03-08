n = int(input())
W = [list(map(int, input().split())) for _ in range(n)]
visited = [False] * n
answer = 1e9

def dfs(node, x, cost):
    global answer

    if x == n:
        if W[node][0]:
            answer = min(answer, cost + W[node][0])
        return

    for next_node in range(1, n):
        if W[node][next_node] and not visited[next_node]:
            visited[next_node] = True
            dfs(next_node, x + 1, cost + W[node][next_node])
            visited[next_node] = False

dfs(0, 1, 0)
print(answer)