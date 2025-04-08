def distChar(s1, s2):
    def create_char_set(s):
        char_set = [False] * 26
        for char in s:
            index = ord(char) - ord('a')
            char_set[index] = True
        return char_set
    
    def sort_distinct_chars(set1, set2):
        result = ''
        for i in range(26):
            if set1[i] != set2[i]:
                result += chr(i + ord('a'))
        return result
    
    s1_chars = create_char_set(s1)
    s2_chars = create_char_set(s2)
    
    return sort_distinct_chars(s1_chars, s2_chars)

def main():
    test_cases = [
        ('characters', 'alphabets'),
        ('apples', 'oranges'),
        ('apples', 'apples'),
        ('hello', 'world'),
        ('programming', 'coding')
    ]
    
    for s1, s2 in test_cases:
        result = distChar(s1, s2)
        print(f"distChar('{s1}', '{s2}') -> '{result}'")

if __name__ == "__main__":
    main()