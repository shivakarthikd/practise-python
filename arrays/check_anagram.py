

def check_anagram(s1,s2):
    i=0
    s1=s1.replace(" ","").lower()
    s2 = s2.replace(" ", "").lower()

    if len(s1) != len(s2):
        return False

    while(True):

        if s1[i] in s2:
            i=i+1
        else:
            break

        if i==len(s2):
            return True
    return False

def check_anagram2(s1,s2):
    d=s=dict()

    for i in s1:
        if i != ' ':
            d[i]=s1.count(i)
    for i in s2:
        if i!=' ':
            s[i]=s2.count(i)
    print(d,s)


print(check_anagram2("thar kik","karthik"))