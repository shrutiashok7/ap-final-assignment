def minOp(str1, str2):
    m = len(str1)
    n = len(str2)
    
    dp = []
    for i in range(m + 1):
        dp.append([0] * (n + 1))
    
    for i in range(m + 1):
        dp[i][0] = i
    
    for j in range(n + 1):
        dp[0][j] = j
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j],    # Remove
                                   dp[i][j-1],    # Insert
                                   dp[i-1][j-1])  # Replace
    
    return dp[m][n]

def main():
    test_cases = [
        ('python', 'pythons'),
        ('abc', ''),
        ('abc', 'def'),
        ('ab', 'def')
    ]
    
    for str1, str2 in test_cases:
        result = minOp(str1, str2)
        print(f"minOp('{str1}', '{str2}') -> {result}")

if __name__ == "__main__":
    main()