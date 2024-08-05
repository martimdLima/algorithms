class Solution:
    # Using heron's Area Formula
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        """
        Calculate all possible triangle areas from a list of points.

        Parameters:
        points (list): List of coordinates of the points.

        Returns:
        list: List of areas of all possible triangles.
        """

        def calculate_distance(
            point1: Tuple[float, float], point2: Tuple[float, float]
        ) -> float:
            """
            Calculate the Euclidean distance between two points (x1, y1) and (x2, y2).

            Parameters:
            point1 (tuple): Coordinates of the first point (x1, y1).
            point2 (tuple): Coordinates of the second point (x2, y2).

            Returns:
            float: The Euclidean distance between the two points.
            """
            x1, y1 = point1
            x2, y2 = point2
            return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

        def triangle_area(
            point1: Tuple[float, float],
            point2: Tuple[float, float],
            point3: Tuple[float, float],
        ) -> float:
            """
            Calculate the area of a triangle given its three vertices using Heron's formula:
                - s = (a+b+c)/2

            Parameters:
            point1, point2, point3 (tuple): Coordinates of the triangle's vertices.

            Returns:
            float: The area of the triangle.
            """
            a = calculate_distance(point1, point2)
            b = calculate_distance(point2, point3)
            c = calculate_distance(point3, point1)

            semi_perimeter = (a + b + c) / 2

            area = math.sqrt(
                semi_perimeter
                * abs(semi_perimeter - a)
                * abs(semi_perimeter - b)
                * abs(semi_perimeter - c)
            )
            return area

        largest_area = 0
        for combination in combinations(points, 3):
            point1, point2, point3 = combination
            area = triangle_area(point1, point2, point3)
            largest_area = max(largest_area, area)

        return largest_area

    # Using Gauss's Area Formula
    def largestTriangleArea(points: List[List[int]]) -> float:
        def gauss_area_formula(
            point1: Tuple[int, int], point2: Tuple[int, int], point3: Tuple[int, int]
        ) -> float:
            x1, y1 = point1
            x2, y2 = point2
            x3, y3 = point3
            return 0.5 * abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))

        largest_area = 0
        for combination in combinations(points, 3):
            point1, point2, point3 = combination
            area = gauss_area_formula(point1, point2, point3)
            largest_area = max(largest_area, area)

        return largest_area
