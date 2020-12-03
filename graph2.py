def removeStones(stones):

    c=0
    vis= [0]*len(stones)
    ls=[]
    v={}
    for i in range(0,len(stones)):
      #  ls.append(stones[i])
        ls=[]
        for j in range(0,len(stones)):
            #ls[c]=list()
            if stones[j] not in ls:
             if (stones[i][0]==stones[j][0] or stones[i][1]==stones[j][1]) :

                    if not vis[j]:
                        vis[j]=1
                        i=j
                    ls.append(stones[j])
                    if set(stones[j]) & set(v.values()[c][0]) or stones[j][1]==v.values()[c][]:

                        v={c:[k for k in ls]}

       # c=c+1
        print(vis)
        print(ls)
   # print([l for l in ls if l. < 0])
    if len(stones)==len(ls):
        return len(stones)-1
    else:
        return len(stones)-(len(stones)-len(ls))-len([i for i in vis if i < 1])
    #return len(stones)-count

print(removeStones([[3,2],[3,1],[4,4],[1,1],[0,2],[4,0]]))