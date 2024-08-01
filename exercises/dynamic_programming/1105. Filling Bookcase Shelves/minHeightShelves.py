class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        bookcase = [0] * (len(books) + 1)
        minimum_total_height = 0

        for idx, (width, height) in enumerate(books, 1):
            minimum_total_height = bookcase[idx - 1] + height
            bookcase[idx] = minimum_total_height

            total_width = width
            for j in range(idx - 1, 0, -1):
                total_width += books[j - 1][0]

                if total_width > shelfWidth:
                    break

                height = max(height, books[j - 1][1])
                bookcase[idx] = min(bookcase[idx], bookcase[j - 1] + height)

        return bookcase[-1]

    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        num_books = len(books)
        shelves = [float("inf")] * (num_books + 1)
        shelves[0] = 0

        for i in range(1, num_books + 1):
            width = 0
            height = 0
            j = i - 1

            while j >= 0 and width + books[j][0] <= shelfWidth:
                width += books[j][0]
                height = max(height, books[j][1])

                current_shelf_height = height
                previous_minimum_height = shelves[j]
                current_minimum_height = shelves[i]

                shelves[i] = min(
                    current_minimum_height,
                    previous_minimum_height + current_shelf_height,
                )
                j -= 1

        return shelves[num_books]
