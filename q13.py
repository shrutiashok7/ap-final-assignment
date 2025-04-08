def check(s, k):
    if len(s) <= k:
        return ""
    
    char_count = [0] * 26
    for char in s:
        index = ord(char) - ord('a')
        char_count[index] += 1
    
    distinct_chars = 0
    for count in char_count:
        if count > 0:
            distinct_chars += 1
    
    best_result = ""
    best_distinct = 0
    
    for target_count in range(1, len(s) + 1):
        chars_to_remove = 0
        possible = True
        potential_result = [''] * 26
        
        for i in range(26):
            if char_count[i] == 0:
                continue
                
            if char_count[i] < target_count:
                possible = False
                break
                
            if char_count[i] > target_count:
                chars_to_remove += char_count[i] - target_count
                
            char = chr(i + ord('a'))
            potential_result[i] = char * target_count
        
        if possible and chars_to_remove == k:
            result_str = ''.join(potential_result)
            current_distinct = sum(1 for c in potential_result if c)
            
            if current_distinct > best_distinct:
                best_distinct = current_distinct
                best_result = result_str
    
    return best_result

def main():
    test_cases = [
        ('aabbcc', 0),
        ('aabbbcc', 0),
        ('aabbbcc', 1),
        ('aabbbcc', 3),
        ('aabbbcc', 4),
        ('aabbbcc', 5),
        ('aabbbcc', 6),
        ('aabbbcc', 7),
        ('aaaabbcc', 4)
    ]
    
    for s, k in test_cases:
        result = check(s, k)
        if result:
            print(f"check('{s}', {k}) -> '{result}'")
        else:
            print(f"check('{s}', {k}) -> ''")

if __name__ == "__main__":
    main()