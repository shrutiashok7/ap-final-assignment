def splitsum(l):
    return [sum([num**2 for num in l if num > 0]), sum([num**3 for num in l if num < 0])]

print(splitsum([1, -2, 3, -4, 5]))
print(splitsum([2, 4, 6]))
print(splitsum([-1, -3, -5]))