class LengthMismatchException(Exception):
    pass

def weave(list1, list2):
    if len(list1) != len(list2):
        raise LengthMismatchException("Lists must have equal length")
    
    result = []
    for i in range(len(list1)):
        result.append(list1[i])
    
    for i in range(len(list2)):
        result.append(list2[i])
    
    return result