def moveDups(s):
    if not s:
        return s
    
    seen = [False] * 26
    first_occurrence = ''
    duplicates = ''
    
    for char in s:
        index = ord(char) - ord('a')
        if not seen[index]:
            first_occurrence += char
            seen[index] = True
        else:
            duplicates += char
    
    if not duplicates:
        return s
    
    return first_occurrence + '_' + duplicates

def main():
    test_cases = [
        'cartoon',
        'network',
        'aabbcc',
        'cccbbaaa',
        'programming',
        'hello'
    ]
    
    for case in test_cases:
        result = moveDups(case)
        print(f"moveDups('{case}') -> '{result}'")

if __name__ == "__main__":
    main()