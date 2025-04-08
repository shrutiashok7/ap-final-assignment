def delDup(l):
    result = []
    
    for num in l:
        if num not in result:
            result.append(num)
    
    return result
