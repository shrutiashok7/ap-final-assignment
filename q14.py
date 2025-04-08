def equivalent(str1, str2):
    def are_rotationally_equivalent(s1, s2):
        if len(s1) != len(s2):
            return False
        
        extended = s1 + s1
        return s2 in extended
    
    n1, n2 = len(str1), len(str2)
    max_length = 0
    result = ""
    
    for length in range(min(n1, n2), 0, -1):
        candidates = []
        
        for i in range(n1 - length + 1):
            substr1 = str1[i:i+length]
            
            for j in range(n2 - length + 1):
                substr2 = str2[j:j+length]
                
                if are_rotationally_equivalent(substr1, substr2):
                    candidates.append(substr1)
        
        if candidates:
            candidates.sort()
            return candidates[0]
    
    return ""

def main():
    test_cases = [
        ('hdjkoul', 'pokoudj'),
        ('ghajiop', 'abkoidj'),
        ('hdjkoul', 'pikpiaa')
    ]
    
    for str1, str2 in test_cases:
        result = equivalent(str1, str2)
        if result:
            print(f"equivalent('{str1}', '{str2}') -> '{result}'")
        else:
            print(f"equivalent('{str1}', '{str2}') -> ''")

if __name__ == "__main__":
    main()