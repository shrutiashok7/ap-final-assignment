class InvalidArgumentError(Exception):
    def __init__(self, message="Arguments must be non-negative integers"):
        self.message = message
        super().__init__(self.message)

def shift(s, ccount=0, acount=0):
    if not (isinstance(ccount, int) and isinstance(acount, int)):
        raise InvalidArgumentError("Arguments must be integers")
    
    if ccount < 0 or acount < 0:
        raise InvalidArgumentError()
    
    length = len(s)
    
    if length == 0:
        return s
    
    ccount = ccount % length
    acount = acount % length
    
    def rotate_left(string, count):
        return string[count:] + string[:count]
    
    def rotate_right(string, count):
        return string[-count:] + string[:-count]
    
    rotated_s = rotate_left(s, acount)
    final_s = rotate_right(rotated_s, ccount)
    
    return final_s

def main():
    test_cases = [
        ('NinjaHattori',),
        ('NinjaHattori', 0, 3),
        ('NinjaHattori', 3, 0),
        ('NinjaHattori', 3, 3),
        ('NinjaHattori', 6, 3),
        ('NinjaHattori', 3, 6)
    ]
    
    for args in test_cases:
        try:
            result = shift(*args)
            print(f"shift{args} -> '{result}'")
        except InvalidArgumentError as e:
            print(f"Error for {args}: {e.message}")
    
    print("\nding ding")

if __name__ == "__main__":
    main()