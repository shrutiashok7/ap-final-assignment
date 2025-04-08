class DimensionMismatchException(Exception):
    pass

def printMat(matrix):
    n = len(matrix)
    
    root = int(n ** 0.5)
    if root * root != n:
        found = False
        for rows in range(2, n):
            if n % rows == 0:
                cols = n // rows
                found = True
                break
        
        if not found:
            raise DimensionMismatchException("Cannot form a rectangular matrix")
    else:
        rows = root
        cols = root
    
    for i in range(0, n, cols):
        row = matrix[i:i+cols]
        print(' '.join(map(str, row)))

# Example
printMat([1, 2, 0, 4, 0, 5, 0, 7, 9])