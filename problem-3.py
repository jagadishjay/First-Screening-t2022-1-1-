n = int(input())
value = 1
if n%2==0:
    n=n-1
while (n>0): 
    print(value,end = " ")
    value = value+2
    n=n-1