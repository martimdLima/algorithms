class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates) < 3:
            return True

        (x1, y1), (x2, y2) = coordinates[0], coordinates[1]

        for i in range(2, len(coordinates)):
            x3, y3 = coordinates[i]
            points_are_not_collinear = (x2 - x1) * (y3 - y1) != (y2 - y1) * (x3 - x1)
            if points_are_not_collinear:
                return False
        return True
