def firstLetters(s):
    result = ''
    is_new_word = True
    
    for char in s:
        if char == ' ':
            is_new_word = True
        elif is_new_word:
            result += char
            is_new_word = False
    
    return result

def main():
    test_cases = [
        'bad is nice',
        'hello other world',
        'python programming language',
        'quick brown fox'
    ]
    
    for sentence in test_cases:
        result = firstLetters(sentence)
        print(f"firstLetters('{sentence}') -> '{result}'")

if __name__ == "__main__":
    main()