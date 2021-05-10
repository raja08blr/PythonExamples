def convertList2Number(li):
    lis_num = ''.join(map(str,li))
    print(lis_num)
    lis_num_add = int(lis_num) +1
    lis_add_str= str(lis_num_add)

    post_add_l = []
    post_add_str = ""

    for i in range(len(lis_add_str)):
        if lis_add_str[i] == '_':
            post_add_str= post_add_str+i
        elif i ==1:
            post_add_str+=i
            post_add_l.append(post_add_str)
        else:
            post_add_l.append(lis_add_str[i])
    print("post addition:: ",post_add_l)


convertList2Number([-2,0,0])