

def word_split(word,ls,output=None):
    if output is None:
        output=[]

    for i in ls:
        if word.startswith(i):
            output.append(i)

            return word_split(word[len(i):],ls,output)
    return output


print(word_split("karmaisgood",['good','karma','is']))