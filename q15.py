def subPali(s):
    if not s:
        return 0
    
    max_length = 1
    n = len(s)
    
    for center in range(n):
        left = center - 1
        right = center + 1
        
        while left >= 0 and right < n and s[left] == s[right]:
            current_length = right - left + 1
            max_length = max(max_length, current_length)
            left -= 1
            right += 1

    for center in range(n - 1):
        left = center
        right = center + 1
        
        while left >= 0 and right < n and s[left] == s[right]:
            current_length = right - left + 1
            max_length = max(max_length, current_length)
            left -= 1
            right += 1
    
    return max_length