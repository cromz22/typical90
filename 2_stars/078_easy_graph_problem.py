n, m = map(int, input().split())

graph = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)

counter = 0
for i, elem in enumerate(graph):
    inner_counter = 0
    for num in elem:
        if num < i:
            inner_counter += 1
    if inner_counter == 1:
        counter += 1

print(counter)
