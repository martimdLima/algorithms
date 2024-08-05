class Solution:
    def findTheCity(
        self, n: int, edges: List[List[int]], distanceThreshold: int
    ) -> int:
        def dijkstra(graph, src):
            n = len(graph)
            distances = [float("inf")] * n
            visited = [False] * n
            distances[src] = 0

            for _ in range(n):
                # Find the unvisited node with the smallest distance
                min_distance = float("inf")
                min_index = -1
                for i in range(n):
                    if not visited[i] and distances[i] < min_distance:
                        min_distance = distances[i]
                        min_index = i

                # If no node is found, break the loop
                if min_index == -1:
                    break

                # Mark the node as visited
                visited[min_index] = True

                # Update distances of the adjacent nodes
                for j in range(n):
                    if graph[min_index][j] != float("inf") and not visited[j]:
                        new_distance = distances[min_index] + graph[min_index][j]
                        if (
                            new_distance <= distanceThreshold
                            and new_distance < distances[j]
                        ):
                            distances[j] = new_distance

            return sum(d <= distanceThreshold for d in distances)

        # Create the adjacency matrix
        graph = [[float("inf")] * n for _ in range(n)]
        for i in range(n):
            graph[i][i] = 0  # Distance to itself is 0

        for edge in edges:
            u, v, weight = edge
            graph[u][v] = weight
            graph[v][u] = weight  # Since the graph is bidirectional

        min_reachable_cities = float("inf")
        result_city = n

        for src in range(n):
            reachable_cities = dijkstra(graph, src)

            if reachable_cities <= min_reachable_cities:
                min_reachable_cities = reachable_cities
                result_city = src

        return result_city

    def findTheCity(
        self, n: int, edges: List[List[int]], distanceThreshold: int
    ) -> int:
        def dijkstra(graph, src):
            distances = [float("inf")] * n
            distances[src] = 0
            min_heap = [(0, src)]  # (distance, node)

            while min_heap:
                current_distance, node = heappop(min_heap)

                if current_distance > distances[node]:
                    continue

                for weight, vertex in graph[node]:
                    new_distance = current_distance + weight

                    if (
                        new_distance < distances[vertex]
                        and new_distance <= distanceThreshold
                    ):
                        distances[vertex] = new_distance
                        heappush(min_heap, (new_distance, vertex))

            return sum(d <= distanceThreshold for d in distances)

        # Create the adjacency list
        graph = [[] for _ in range(n)]
        for node, vertex, weight in edges:
            graph[node].append((weight, vertex))
            graph[vertex].append((weight, node))  # Since the graph is bidirectional

        min_reachable_cities = float("inf")
        result_city = n

        for src in range(n):
            reachable_cities = dijkstra(graph, src)
            if reachable_cities <= min_reachable_cities:
                min_reachable_cities = reachable_cities
                result_city = src

        return result_city
