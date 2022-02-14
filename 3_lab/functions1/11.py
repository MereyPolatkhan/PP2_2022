def isPalindrome(s):
    reversed_s = s[::-1]
    if reversed_s == s:
        return True
    else:
        return False

print(isPalindrome('madam'))