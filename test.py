def func(n):
    a=0
    for i in range(1,n):
        a = a+i
        print(a, end=' ')

f = func
print(f(0))