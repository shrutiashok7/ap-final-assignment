def list_operations(integers):
    print(integers[3])
    
    print(integers[2:])
    
    print(integers[::-1])
    
    total = 0
    for num in integers:
        total += num
    print(total)
    
    maximum = integers[0]
    minimum = integers[0]
    for num in integers:
        if num > maximum:
            maximum = num
        if num < minimum:
            minimum = num
    print(maximum, minimum)
    
    zero_index = -1
    for i in range(len(integers)):
        if integers[i] == 0:
            zero_index = i
            break
    print(zero_index)
    
    asc_sorted = integers.copy()
    for i in range(len(asc_sorted)):
        for j in range(i + 1, len(asc_sorted)):
            if asc_sorted[i] > asc_sorted[j]:
                asc_sorted[i], asc_sorted[j] = asc_sorted[j], asc_sorted[i]
    print(asc_sorted)
    
    desc_sorted = integers.copy()
    for i in range(len(desc_sorted)):
        for j in range(i + 1, len(desc_sorted)):
            if desc_sorted[i] < desc_sorted[j]:
                desc_sorted[i], desc_sorted[j] = desc_sorted[j], desc_sorted[i]
    print(desc_sorted)

# Example usage
list_operations([5, 10, 15, 20, 25, 0, 30])