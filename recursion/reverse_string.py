def rev_string(s,i=-1):

    if abs(i)==len(s):
        return s[0]
    else:
        return s[i]+rev_string(s,i-1)


def rev_string_1(s):
    if len(s)<=1:
        return s
    return rev_string_1(s[1:])+s[0]
print(rev_string_1("hitech"))
k="kart"
print(k[::-2])