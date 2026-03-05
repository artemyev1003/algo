from collections import deque


def dfs(tree, node, visited=None):
    if visited is None:
        visited = []

    visited.append(node)

    for child in tree[node]:
        if child not in visited:
            dfs(tree, child, visited)

    return " ".join(map(str, visited)) 

def bfs(tree, node):
    visited = []
    queue = deque([node])

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            for child in tree[node]:
                if child not in visited:
                    queue.append(child)
    return " ".join(map(str, visited))


n, m, vortex = map(int, input().split())
tree = {node: [] for node in range(1, n + 1)}
for edge in range(m):
    node, child = map(int, input().split())
    tree[node].append(child)
    tree[child].append(node)

for node in tree:
    tree[node].sort()

print(dfs(tree, vortex))
print(bfs(tree, vortex))
