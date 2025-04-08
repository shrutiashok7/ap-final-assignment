def checkPalindrome(s):
    start = 0
    end = len(s) - 1
    
    while start < end:
        if s[start] != s[end]:
            return False
        start += 1
        end -= 1
    
    return True

def main():
    test_strings = ["madam", "racecar", "hello", "python", "level"]
    
    for word in test_strings:
        if checkPalindrome(word):
            print(f"{word} is a palindrome")
        else:
            print(f"{word} is not a palindrome")

if __name__ == "__main__":
    main()