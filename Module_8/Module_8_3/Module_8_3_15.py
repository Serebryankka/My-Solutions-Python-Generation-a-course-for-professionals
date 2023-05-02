def is_palindrome(string):
    def rec(s):
        if not s:
            return s
        else:
            return s[-1] + rec(s[:-1])
    return rec(string) == string
