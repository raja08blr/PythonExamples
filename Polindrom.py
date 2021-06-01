s="MalaalaM"
for i in range(len(s)/2):
    if s[i] != s[(len(s)/2)-i-1]:
        print("Polyndrom")