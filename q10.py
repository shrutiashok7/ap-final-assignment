def separate(s):
    if not s:
        return []
    
    result = []
    current_group = s[0]
    
    for i in range(1, len(s)):
        if s[i] == current_group[0]:
            current_group += s[i]
        else:
            result.append(current_group)
            current_group = s[i]
    
    result.append(current_group)
    
    return result

def main():
    test_cases = [
        'cartoon',
        'network',
        'aabbcc',
        'cccbbaaa'
    ]
    
    for case in test_cases:
        result = separate(case)
        print(f"separate('{case}') -> {result}")

if __name__ == "__main__":
    main()