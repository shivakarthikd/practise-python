import collections
def compress_string(st):
    c_dic=collections.defaultdict(int)
    c_str=''
    for i in st:
        c_dic[i]+=1

    for key,val in c_dic.items():
        c_str= c_str+ key + str(val)
    print(c_str)


def compress_string_1(st):
    c_str=''
    c=0
    while(c<len(st)):
        count=0
        for i in st:
            if st[c]==i:
                count +=1
        if st[c] not in c_str:
            c_str+=st[c]+str(count)
        c+=1
    print(c_str)


def compress(s):
    """
    This solution compresses without checking. Known as the RunLength Compression algorithm.
    """

    # Begin Run as empty string
    r = ""
    l = len(s)

    # Check for length 0
    if l == 0:
        return ""

    # Check for length 1
    if l == 1:
        return s + "1"

    # Intialize Values
    last = s[0]
    cnt = 1
    i = 1

    while i < l:

        # Check to see if it is the same letter
        if s[i] == s[i - 1]:
            # Add a count if same as previous
            cnt += 1
        else:
            # Otherwise store the previous data
            r = r + s[i - 1] + str(cnt)
            cnt = 1

        # Add to index count to terminate while loop
        i += 1

    # Put everything back into run
    r = r + s[i - 1] + str(cnt)

    return r



print(compress('AbbAA'))