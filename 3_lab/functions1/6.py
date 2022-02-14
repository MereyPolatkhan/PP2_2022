def func_reverse(s):
    a = s.split() 
    a.reverse() 
    print(' '.join(a))

s = input()
func_reverse(s)