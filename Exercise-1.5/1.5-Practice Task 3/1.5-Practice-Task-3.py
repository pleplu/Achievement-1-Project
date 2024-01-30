
# In the preceding code, methods are defined for the less than (<), less than or equal to (<=) and equal to (==) operators. 
# Now try to define a few more for the greater than (>), greater than or equal to (>=) and not equal to (!=) operators.

# Test your new methods against the following test cases:
 
# Height(4, 6) > Height(4, 5)
# Height(4, 5) >= Height(4, 5)
# Height(5, 9) != Height(5, 10)

class Height(object):
    def __init__(self, feet, inches):
        self.feet = feet
        self.inches = inches

    def __gt__(self, other):
        height_inches_A = self.feet * 12 + self.inches
        height_inches_B = other.feet * 12 + other.inches
        return height_inches_A > height_inches_B



    def __ge__(self, other):
        height_inches_A = self.feet * 12 + self.inches
        height_inches_B = other.feet * 12 + other.inches
        return height_inches_A >= height_inches_B



    def __ne__(self, other):
        height_inches_A = self.feet * 12 + self.inches
        height_inches_B = other.feet * 12 + other.inches
        return height_inches_A != height_inches_B

# Output:

# Height(4, 6) > Height(4, 5)
# True

# Height(4, 5) >= Height(4, 5)
# True

# Height(5, 9) != Height(5, 10)
# True