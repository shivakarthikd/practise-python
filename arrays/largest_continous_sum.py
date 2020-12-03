def find_sum(arr):
    curr_sum=max_sum=arr[0]
    for i in arr[1:]:
        curr_sum=max(i+curr_sum,i)
        max_sum=max(curr_sum,max_sum)
    print(max_sum)

def find_sum_2(arr):
    max_sum=arr[0]
    curr_sum=0
    for i in arr:
        curr_sum += i
        if curr_sum < 0:
            curr_sum=i
        if max_sum<curr_sum:
            max_sum=curr_sum
    print(max_sum)

find_sum_2([-9,-3,-1,-8,-5])

