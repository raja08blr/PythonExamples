given_string = "Python is an interpreted,high-level,general-purposeprogramminglanguage.Created by Guido van Rossumandfirstreleased in 1991, Python's design philosophy emphasizes code readability with its notable use of significant whitespace."


def char_count(string):
    dic = {}
    for char in string:
        if char not in dic:
            dic[char] = 1
        else:
            dic[char] += 1
    return dic


result = char_count(given_string.lower())
print(result)
# list = []
max = 0

for i, k in result.items():

    if k > max:
        max = k
        max_char = i
print(max, max_char)

result1 = sorted(result.items(), key=lambda x:x[-1]) #ascending
print("ascending",result1)
print("Highest count char",result1[-1])

des = sorted(result.items(), key=lambda x:x[1],reverse=True) #ascending
print("desending",des)
print("Highest count char",des[0])
