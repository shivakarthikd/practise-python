def check_paran(s):
    ls=[]
    val=''
    for i in s:
        if i  in ['[','{','(']:
            ls.append(i)
        else:
          if len(ls)==0:
              return False
          last_open=ls.pop()
          print(last_open,i)
          if (last_open,i) not in [('{','}'),('[',']'),('(',')')]:
              return False
    return len(ls)==0

def check_paran_1(s):
    ls=[]
    count=0
    for i in s:
        count=0

        if i  in ['[','{','(']:
            ls.append(i)
        else:
          if len(ls)==0:
              return False
          last_open=ls.pop()

          for j in s[s.index(i):len(s)]:
            if (last_open,j) in [('{','}'),('[',']'),('(',')')]:
              # print(last_open, j)
              count+=1
    return count


print(check_paran_1("[](){{((({)))}}}"))