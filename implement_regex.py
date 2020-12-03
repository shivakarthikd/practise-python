def imp_reg(s,p):
    if s in p:
        print("substring")
        return True
    i=0
    j=0
    while True:

        if i==len(p):
            return False

        if p=='':
            return False

        if p[i]=='.':
            if i<len(p)-1 and p[i+1] == '*':
                return True
            elif i<len(p)-1 and p[i+1].isalpha():
                if p[i+1] in s:
                    j=j+1
                    i=i+1
                    continue

        if p[i] in s:
            if i < len(p)-1 and p[i+1]=='*':
                i=i+1
                j=j+1
                continue
            if i==len(p):


            print(i)
            j=j+1
        if j+1==len(s):
            return True
        i=i+1
    return False

s="aab"
p="c*a*b"

print(imp_reg(s,p))
print(imp_reg("aa","a"))