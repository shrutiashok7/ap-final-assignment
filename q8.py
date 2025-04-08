def delVowels(s):
    vowels = 'aeiouAEIOU'
    result = ''
    
    for char in s:
        is_vowel = False
        
        for v in vowels:
            if char == v:
                is_vowel = True
                break
        
        if not is_vowel:
            result += char
    
    return result

def main():
    test_cases = [
        'SfgEtfjofubjiekp',
        'aEiOu',
        'Hello World',
        'Python Programming',
        'AEIOU CONSONANTS'
    ]
    
    for case in test_cases:
        result = delVowels(case)
        print(f"delVowels('{case}') -> '{result}'")

if __name__ == "__main__":
    main()