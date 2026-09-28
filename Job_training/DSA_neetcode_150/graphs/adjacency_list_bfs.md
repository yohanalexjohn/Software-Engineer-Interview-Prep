# Adjacency-List BFS Traversal

## Prompt

Given an adjacency-list graph and a start vertex, return all reachable vertices in breadth-first order.

## Approach

Put the start vertex in a queue and mark it visited. Repeatedly remove the front vertex, process it, and enqueue each unseen neighbour.

## Key invariant

Every queued vertex is already marked visited. Therefore each reachable vertex is enqueued at most once and the queue proceeds in increasing edge distance.

## Complexity

- Time: O(V + E).
- Space: O(V).

## Common mistakes

- Marking visited when popping, which permits duplicate queue entries.
- Forgetting disconnected vertices require an outer loop when the task asks for every component.
- Confusing tree children with graph neighbours.

```cpp
vector<int> bfs(const vector<vector<int>>& graph, int start)
{
    vector<int> order;
    vector<bool> visited(graph.size(), false);
    queue<int> q;
    visited[start] = true;
    q.push(start);

    while (!q.empty()) {
        int current = q.front();
        q.pop();
        order.push_back(current);
        for (int neighbour : graph[current]) {
            if (!visited[neighbour]) {
                visited[neighbour] = true;
                q.push(neighbour);
            }
        }
    }
    return order;
}
```
