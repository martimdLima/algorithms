class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:

        bulky = (length >= 10000 or width >= 10000 or height >= 10000) or ((length*width*height)>=1000000000)
        heavy = mass >= 100

        if bulky and heavy:
            return "Both"

        if not bulky and not heavy:
            return "Neither"

        if bulky and not heavy:
            return "Bulky"
        
        if not bulky and heavy:
            return "Heavy"