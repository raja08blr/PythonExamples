import pandas as pd

d = pd.Series(['a', 'bb', 'ccc'])
print(d)
print(d.map(lambda x: x.title()))

#calculate number character in each word
print(d.map(lambda x:len(x)))

# print longest substring

l=['a','bb','cvvvv']
print(max(l,key=len))
