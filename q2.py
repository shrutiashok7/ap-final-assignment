def minIndexFirstString(str1, str2):
    max_index = -1
    
    for i in range(len(str1)):
        for j in range(len(str2)):
            if str1[i] == str2[j]:
                max_index = max(max_index, i)
                break
    
    return max_index

def main():
    test_cases = [
        ('tiger', 'integer'),
        ('integer', 'tiger'),
        ('hello', 'world'),
        ('python', 'javascript')
    ]
    
    for s1, s2 in test_cases:
        result = minIndexFirstString(s1, s2)
        print(f"minIndexFirstString('{s1}', '{s2}') -> {result}")

if __name__ == "__main__":
    main()