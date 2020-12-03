def findCircleNum(M) :
    ls=[[]]
    ks=[]
    start=0
    dict={}
    for i in range(start,len(M)):
        for j in range(start,len(M[i])):
            if M[i][j] == 1:
                if i in dict.keys():
                    dict.get(i).append(j)
                else:
                    dict[i] = [j]
        start=start+1
    print(dict)
    for k in dict:
        for v in dict.values():
            print(dict.get(k),v)
            if len(list(set(dict.get(k)) & set(v)))>0:

                ls.append([k])



    return ls

print(findCircleNum([[1,1,0],[1,1,0],[0,0,1]]))