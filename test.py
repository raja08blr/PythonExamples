
def FirstDuplicateCharinString(str1):
    rep_char={}
    for char in str1:
        if char in rep_char:
            return char
        else:
            rep_char[char]=1
    # return '\0'
            # break
    # print("First duplicate character:: ",rep_char)
print(FirstDuplicateCharinString("rajaja"))

def NonDuplicateCharacters(st):
    non_dup = []
    for char in st:
        if char not in non_dup:
            non_dup.append(char)
    print(non_dup)
NonDuplicateCharacters("rajaa")



# pair for given number


def get_Pairs_Of_Given_List(d, k):
    op = []
    for i in d:
        if (k-i) in d:
            op.append(((k-i),i))

            d.remove(k-i)
    print(op)

get_Pairs_Of_Given_List([3,4,5,6,7,3], 10)

#####################################################

def convertListToNumberAndAddValueCOnvertReverse(list_1):
    Num_value = ''.join(map(str,list_1))
    print(Num_value)
    Num_value_add = int(Num_value)+1
    s=[]
    r=''
    Num_value_add_str = str(Num_value_add)
    for ele in range(len(Num_value_add_str)):
        if Num_value_add_str[ele] == '-':
            r=r+Num_value_add_str[ele]
        elif ele == 1:
            r=r+Num_value_add_str[ele]
            s.append(r)
        else:
            s.append(Num_value_add_str[ele])
    # print(s)
    return s
# print(convertListToNumberAndAddValueCOnvertReverse([-2,0,0]))
# print(convertListToNumberAndAddValueCOnvertReverse([2,0,0]))
# # print len_list