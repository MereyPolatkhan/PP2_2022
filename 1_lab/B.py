s = str(input())

def is_tasty1(s):
    sum = 0
    for i in range(len(s)):
        sum += ord(s[i])
    if sum >= 300:
        print("It is tasty!")
    else:
        print("Oh, no!")

i = 0
sum = 0
def recursion_is_tasty(s):
    global sum, i
    if(len(s) == i):
        return sum
    sum += ord(s[i])
    i += 1
    return recursion_is_tasty(s)
    
def is_tasty2(s):
    n_from_recursion = recursion_is_tasty(s) 
    if n_from_recursion >= 300:
        print("It is tasty!")
    else:
        print("Oh, no!")

# answer:
is_tasty1(s)
is_tasty2(s)