
class InvalidInputException(Exception):
    def __init__(self, message="Input must be a string of only 'R' and 'G' characters"):
        self.message = message
        super().__init__(self.message)

def change(s):
    if not s:
        return 0
    
    for char in s:
        if char != 'R' and char != 'G':
            raise InvalidInputException()
    
    red_count = 0
    green_count = 0
    
    for char in s:
        if char == 'R':
            red_count += 1
        else:
            green_count += 1
    
    return min(red_count, green_count)

def main():
    test_cases = [
        'R',
        'RGRGR',
        'GRG',
        'RRRGG',
        'GGGRRR',
        'RGRGRG'
    ]
    
    for case in test_cases:
        try:
            result = change(case)
            print(f"change('{case}') -> {result}")
        except InvalidInputException as e:
            print(f"Error for '{case}': {e.message}")
    
    try:
        change('RBG')  # This should raise an exception
    except InvalidInputException as e:
        print(f"Error: {e.message}")

if __name__ == "__main__":
    main()