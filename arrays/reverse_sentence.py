import collections
def reverse_sentence(sentence):
    sentence=sentence.strip(' ')
    sentence=sentence.split(' ')
    print(' '.join(sentence[::-1]))

def reverse_sentence_1(sentence):
    i=0
    rs=''
    ns=''
    while(True):
        if i==len(sentence):
            break
        if sentence[i]!=' ':
            rs=rs+' '.join(sentence[i])
            i=i+1
        elif i>1 and sentence[i-1].isalpha() and sentence[i]==' ':
            ns=rs+' '+ns
            rs=''
            i=i+1
        else:
            i=i+1
    print(len(ns[0:-1]))


reverse_sentence_1("      hello   there is food     ")