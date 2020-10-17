# your code goes here
while True:
    n=int(input())
    if n==0:
        break
    a=list(map(int,input().split()))
    s=0
    c=0
    for i in a:
        s+=i
        c+=abs(s)
    print(c
