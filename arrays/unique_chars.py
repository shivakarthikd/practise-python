def uni_chars(s):
 s=sorted(s)
 i=1
 while(i<len(s)):
    if s[i]==s[i-1]:
         return False
    i=i+1
 return True
def uni_chars_1(s):
    ns=set(s)
    return True if len(ns)==len(s) else False


print(uni_chars('abcdefgra'))
