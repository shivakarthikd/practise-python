def convertHeap(inheap):
    i=1
    while(i*2<len(inheap)):
        if inheap[i] < inheap[i*2]:
            inheap[i],inheap[i*2]=inheap[i*2],inheap[i]
        if inheap[i] < inheap[i * 2+1]:
            inheap[i], inheap[i * 2+1] = inheap[i * 2+1], inheap[i]
        i = i * 2

    return inheap



print(convertHeap([0,1,2,3,4,5,6,7]))
