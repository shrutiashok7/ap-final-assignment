class Vector:
    def __init__(self, values):
        self.__values = list(values)
    
    def __str__(self):
        return f"{len(self.__values)}-dimensional vector: {self.__values}"
    
    def __mul__(self, scalar):
        if not isinstance(scalar, (int, float)):
            raise TypeError("Scalar must be a number")
        return Vector([scalar * x for x in self.__values])
    
    def __rmul__(self, scalar):
        return self.__mul__(scalar)
    
    def __add__(self, other):
        if not isinstance(other, Vector):
            raise TypeError("Can only add another Vector")
        if len(self.__values) != len(other.__values):
            raise ValueError("Vectors must have the same dimension")
        return Vector([self.__values[i] + other.__values[i] for i in range(len(self.__values))])
    
    def __sub__(self, other):
        if not isinstance(other, Vector):
            raise TypeError("Can only subtract another Vector")
        if len(self.__values) != len(other.__values):
            raise ValueError("Vectors must have the same dimension")
        return Vector([self.__values[i] - other.__values[i] for i in range(len(self.__values))])
    
    def __matmul__(self, other):
        if not isinstance(other, Vector):
            raise TypeError("Can only take dot product with another Vector")
        if len(self.__values) != len(other.__values):
            raise ValueError("Vectors must have the same dimension")
        return sum(self.__values[i] * other.__values[i] for i in range(len(self.__values)))