s="aaa bbb ccc ddd eee"
st=""
for char in s:
    if char.isalnum():
        st=st+char
print(st)