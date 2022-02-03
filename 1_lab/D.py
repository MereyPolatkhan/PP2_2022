n = int(input())
c = str(input())

if(c == 'k'):
    p = int(input())
    res = n / 1024 
    print(round(res, p))
    # print("{0:.3f}".format(res))
    # print('%.4f'%res)

if(c == 'b'):
    print(n * 1024)

