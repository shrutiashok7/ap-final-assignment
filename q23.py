class DimensionMismatchException(Exception):
    pass

def matMul(matrix1, matrix2):
    n1 = len(matrix1)
    root1 = int(n1 ** 0.5)
    
    if root1 * root1 == n1:
        rows1 = cols1 = root1
    else:
        found = False
        for rows1 in range(2, n1):
            if n1 % rows1 == 0:
                cols1 = n1 // rows1
                found = True
                break
        
        if not found:
            raise DimensionMismatchException("First matrix cannot form a rectangular matrix")
    
    n2 = len(matrix2)
    root2 = int(n2 ** 0.5)
    
    if root2 * root2 == n2:
        rows2 = cols2 = root2
    else:
        found = False
        for rows2 in range(2, n2):
            if n2 % rows2 == 0:
                cols2 = n2 // rows2
                found = True
                break
        
        if not found:
            raise DimensionMismatchException("Second matrix cannot form a rectangular matrix")
    
    if cols1 != rows2:
        raise DimensionMismatchException("Cannot multiply: dimensions mismatch")
    
    mat1 = []
    for i in range(0, n1, cols1):
        mat1.append(matrix1[i:i+cols1])
    
    mat2 = []
    for i in range(0, n2, cols2):
        mat2.append(matrix2[i:i+cols2])
    
    result = []
    for i in range(rows1):
        for j in range(cols2):
            sum_val = 0
            for k in range(cols1):
                sum_val += mat1[i][k] * mat2[k][j]
            result.append(sum_val)
    
    return result

# Example
print(matMul([1, 2, 0, 4, 0, 5, 0, 7, 9], [1, 2, 0, 4, 0, 5, 0, 7, 9]))