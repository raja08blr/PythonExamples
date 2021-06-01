# Write a one-liner that will count the number of capital letters in a file. Your code should work even if the file is too big to fit in memory.

with open("abc.txt",'r') as f:
    data = f.read()
    cnt=0
    for word in data:
        if word.isupper():
            cnt+=1
    print(cnt)
    print(sum(1 for line in f for character in line if character.isupper()))