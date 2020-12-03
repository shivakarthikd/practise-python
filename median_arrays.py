def findMedianSortedArrays(nums1: list, nums2: list):
    nums1.extend(nums2)
    nums1.sort()
    print(nums1)
    l_array=len(nums1)
    if len(nums1) % 2 != 0:
        return nums1[int(l_array/2)]
    else:
        return int((nums1[int(l_array/2)]+nums1[int(l_array/2)-1])/2)

print(findMedianSortedArrays([1, 3],[2]))