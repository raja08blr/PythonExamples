l_word = ["lamb","swan","sheep","lamb","tiger","swan"]

count = {}
for i in l_word:
    if i in count:
        count[i]+=1
    else:
        count[i]=1

print(count)