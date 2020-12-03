def sum_to_n(n):
    if n>1:
        return n + sum_to_n(n-1)
    else:
        return  1

def sum_of_n(n):
    if n>1:
        return (n%10 + sum_of_n(int(n/10)))
    else:
        return  n



print(sum_of_n(4321))