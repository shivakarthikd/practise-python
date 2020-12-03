import collections
def find_missing(arr1,arr2):
    c_dic=collections.defaultdict(int)
    for i in arr2:
        c_dic[i]+=1

    for i in arr1:
        if c_dic[i]==0:
            print(i)
            return i
        else:
            c_dic[i] -=1

def find_missing_1(arr1,arr2):
   avg=sum(arr1)-sum(arr2)
   print(avg)

find_missing([5,5,7,6,7],[5,7,7])