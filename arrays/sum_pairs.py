

def sum_pairs(arr,k):

    ls=list()
    print(arr)
    print(k)
    val = arr[0]
    index=1
    while(True):

        for i in range(index,len(arr)):
            if (arr[i]+val)==k:
                ls.append((arr[i],val))
        if index==len(arr):
            break
        else:
            val = arr[index]
            index += 1

    print(set(ls))

    return(set(ls))

def sum_pairs_1(arr,k):
    seen=set()
    output=set()
    for i in arr:
        diff=k-i
        if diff not in seen:
            seen.add(i)
        else:
            output.add((min(diff,i),max(diff,i)))
    print('\n'.join(map(str,(output))))



sum_pairs_1([1,2,3,1,0,4],4)



