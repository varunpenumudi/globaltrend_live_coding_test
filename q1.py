# Longest Common Subsequence

def lcs(str1, str2):
    m, n = len(str1), len(str2)

    # creating a (m+1)*(n+1) matrix
    dp = [[0 for _ in range(n+1)] for j in range(m+1)]

    for i in range(1, m+1):
        for j in range(1, n+1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    return dp[m][n]


# Testing the function
if __name__ == "__main__":
    print(lcs("abcde", "ace"))
    print(lcs("abcde", "akbhce"))
    print(lcs("hhjij", "hjjk"))
    print(lcs("hhjij", "hajk"))