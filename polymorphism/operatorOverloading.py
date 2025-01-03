class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        """Overload the + operator for vector addition."""
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        """Overload the - operator for vector subtraction."""
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        """Overload the * operator for scalar multiplication."""
        return Vector(self.x * scalar, self.y * scalar)

    def __str__(self):
        """For a readable string representation."""
        return f"Vector({self.x}, {self.y})"

# Example usage
v1 = Vector(3, 4)
v2 = Vector(1, 2)

# Adding two vectors
v3 = v1 + v2
print(v3)  # Output: Vector(4, 6)

# Subtracting two vectors
v4 = v1 - v2
print(v4)  # Output: Vector(2, 2)

# Scalar multiplication
v5 = v1 * 2
print(v5)  # Output: Vector(6, 8)
