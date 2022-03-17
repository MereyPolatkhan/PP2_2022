s = input()

def palindrome(s):
    if ''.join(reversed(s)) == s: # reversed() --> built in function 
        return True
    else:
        return False

print(palindrome(s))