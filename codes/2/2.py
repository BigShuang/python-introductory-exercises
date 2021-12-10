def is_palindromic(s):
    l = len(s)
    for i in range(l // 2):
        if s[i] != s[l-i-1]:
            return False

    return True


print(is_palindromic("abcbba"))
