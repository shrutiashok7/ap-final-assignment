class InvalidKException(Exception):
    pass

def kMax(l, k):
    if k <= 0 or k > len(l):
        raise InvalidKException("k must be between 1 and the length of the list")
    
    sorted_list = l.copy()
    for i in range(len(sorted_list)):
        for j in range(i + 1, len(sorted_list)):
            if sorted_list[i] < sorted_list[j]:
                sorted_list[i], sorted_list[j] = sorted_list[j], sorted_list[i]
    
    return sorted_list[k - 1]

print(kMax([10, 2, 4, 5, 7, 9], 1))
print(kMax([10, 2, 4, 5, 7, 9], 2))
print(kMax([10, 2, 4, 5, 7, 9], 3))