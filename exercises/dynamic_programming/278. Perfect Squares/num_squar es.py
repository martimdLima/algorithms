class Solution:
    # Start from n and try to subtract perfect squares (1, 4, 9, 16, ...) iteratively.
    # Use BFS to explore all possible ways to reduce n to 0, keeping track of the number of steps taken.
    # The BFS ensures that the first time we reach 0 is through the shortest path, guaranteeing the minimum number of steps.
    def numSquares(self, n):
        visited = [0] * (n + 1)
        squares_queue = []
        ans = sys.maxsize
        squares_queue.append([n, 0])
        visited[n] = 1

        while len(squares_queue) > 0:
            stack = squares_queue[0]
            squares_queue.pop(0)  # Dequeue the first in the queue

            # If the current number is 0, update the answer with the minimum steps found
            if stack[0] == 0:
                ans = min(ans, stack[1])

            # Compute the new number number_steps for each possible perfect square i*i less than or equal to the current number
            i = 1
            while i * i <= stack[0]:
                number_steps = stack[0] - i * i

                if number_steps >= 0 and (
                    visited[number_steps] == 0 or number_steps == 0
                ):
                    visited[number_steps] = 1
                    squares_queue.append([number_steps, stack[1] + 1])
                i += 1

        return ans


def numSquares(n):
    if n <= 0:
        return 0

    # A queue to perform BFS, initialized with the start node (n)
    queue = deque([(n, 0)])
    visited = [False] * (n + 1)
    visited[n] = True

    while queue:
        current, steps = queue.popleft()

        # If the current value is zero, return the number of steps taken
        if current == 0:
            return steps

        # Generate all possible children by subtracting perfect squares
        i = 1
        while i * i <= current:
            next_value = current - i * i
            if next_value >= 0 and not visited[next_value]:
                visited[next_value] = True
                queue.append((next_value, steps + 1))
            i += 1

    return 0
