class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

        player_a = True
        play = 0
        n = len(board)
        m = len(board[0])
        while play <= len(moves) - 1:
            move = moves[play]
            player = "A" if player_a else "B"

            board[move[0]][move[1]] = "X" if player_a else "0"
            for row in board:
                if all(x == row[0] for x in row):
                    return player
            for col in range(m):
                if all(board[row][col] == board[0][col] for row in range(n)):
                    return player
            if all(board[i][i] == board[0][0] for i in range(min(n, m))):
                return player
            if all(board[i][m - 1 - i] == board[0][m - 1] for i in range(min(n, m))):
                return player

            if play == 8:
                return "Draw"

            player_a = not player_a
            play += 1

        return "Pending"

    def tictactoe(self, moves: List[List[int]]) -> str:
        n = 3

        rows = [0] * n
        cols = [0] * n
        diag1 = 0
        diag2 = 0

        for i, move in enumerate(moves):
            player = 1 if i % 2 == 0 else -1
            row, col = move

            # Update the counters
            rows[row] += player
            cols[col] += player

            if row == col:
                diag1 += player

            if row + col == n - 1:
                diag2 += player

            if (
                abs(rows[row]) == n
                or abs(cols[col]) == n
                or abs(diag1) == n
                or abs(diag2) == n
            ):
                return "A" if player == 1 else "B"

        if len(moves) == n * n:
            return "Draw"

        return "Pending"
