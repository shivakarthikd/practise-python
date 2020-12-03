def febo_wihout_rec(n):
    a = 0
    b = 1
    for i in range(n):
      a,b=b,a+b
    return a

def febo_with_rec(n,ls=[]):

    if n==0 or n==1:
        cache[n]=n
        return n
    if cache[n]!=None:
        return cache[n]
    cache[n]=febo_with_rec(n-1)+febo_with_rec(n-2)
    return cache[n]


n=11
cache=[None]*(n+1)
print(febo_with_rec(n))
print(cache)
print(febo_wihout_rec(5))