def primePalindrome(N):
    def isright(x):
        out = 0
        for i in range(2, x):
            if x % i == 0:
                break
        else:
            out = 1
        x = str(x)
        if x[0:] == x[::-1] and out == 1:
            out = 1
        else:
            out = 0
        return out

    for t in range(N, 2 * 10 ^ 8):
        q = isright(t)
        if q == 1:
            return t
print(primePalindrome(13))
