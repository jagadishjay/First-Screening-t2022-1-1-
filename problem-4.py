from collections import defaultdict
list_int =map(int,input().split(","))
def func1():
    return 0
    
dict1 = defaultdict(lambda : 0)
a=[1,2,3,4,5,6,7,8,9]
for i in list_int:
    
    for j in a:
        dict1[str(j)] = dict1[str(j)]
        if i%j==0:
            dict1[str(j)] = dict1[str(j)]+1

dict1=dict(sorted(dict1.items()))
print(dict1)
