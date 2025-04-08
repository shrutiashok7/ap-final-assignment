def moveZeros(nums):
    return [num for num in nums if num != 0] + [0] * nums.count(0)

print(moveZeros([1, 2, 0, 4, 0, 5, 0]))