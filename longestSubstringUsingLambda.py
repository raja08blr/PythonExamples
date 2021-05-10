abc=['hello','world','123', 'bac123','123456']
em=[]
# print(list(filter(lambda x: max(str,key=len),abc)))
(print(max(abc, key=lambda s: (len(s), s))))