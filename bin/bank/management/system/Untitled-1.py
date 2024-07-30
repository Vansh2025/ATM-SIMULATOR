def find_largest_sum_cycle(N, edges):
    from collections import defaultdict

    # Create an adjacency list
    graph = defaultdict(list)
    for i, edge in enumerate(edges):
        if edge != -1:
            graph[i].append(edge)

    # Helper function to perform DFS
    def dfs(node, visited, stack, current_sum):
        if node in stack:  # Cycle detected
            cycle_sum = current_sum - visited[node]
            return cycle_sum

        if node in visited:
            return -1  # Already visited, no cycle

        visited[node] = current_sum
        stack.add(node)
        if node in graph:
            for neighbor in graph[node]:
                cycle_sum = dfs(neighbor, visited, stack, current_sum + neighbor)
                if cycle_sum != -1:
                    return cycle_sum

        stack.remove(node)
        return -1

    # Main logic to find the largest sum cycle
    largest_sum_cycle = -1
    visited = {}
    for i in range(N):
        if i not in visited:
            cycle_sum = dfs(i, visited, set(), i)
            if cycle_sum != -1:
                largest_sum_cycle = max(largest_sum_cycle, cycle_sum)

    return largest_sum_cycle

# Input Reading
if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()
    N = int(data[0])
    edges = list(map(int, data[1:]))
    result = find_largest_sum_cycle(N, edges)
print(result)