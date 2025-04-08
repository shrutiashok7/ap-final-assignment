class UpperCaseException(Exception):
    def __init__(self, message="Input string contains uppercase letters"):
        self.message = message
        super().__init__(self.message)

def evenIndexCapital(s):
    result = ''
    
    for i in range(len(s)):
        if s[i] < 'a' or s[i] > 'z':
            raise UpperCaseException()
        
        if i % 2 == 0:
            result += chr(ord(s[i]) - 32)
        else:
            result += s[i]
    
    return result

def main():
    test_cases = [
        'school',
        'python',
        'programming'
    ]
    
    try_cases = test_cases + ['School', 'HELLO']
    
    for sentence in test_cases:
        try:
            result = evenIndexCapital(sentence)
            print(f"evenIndexCapital('{sentence}') -> '{result}'")
        except UpperCaseException as e:
            print(f"Error for '{sentence}': {e.message}")
    
    print("\nTesting uppercase exceptions:")
    for sentence in try_cases:
        try:
            result = evenIndexCapital(sentence)
            print(f"evenIndexCapital('{sentence}') -> '{result}'")
        except UpperCaseException as e:
            print(f"Error for '{sentence}': {e.message}")

if __name__ == "__main__":
    main()