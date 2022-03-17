t = (True, True, True)
t1 = (False, True, True)
t2 = ("", True, True)

print(type(t))
print(all(t))
print(all(t1))
print(all(t2))

# all is built in func

# <class 'tuple'>
# True
# False
# False