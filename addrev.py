# your code goes here
for _ in range(int(input())):
    n=input().split()
    a=n[0]
    b=(n[1])
    d=a[::-1]
    c=b[::-1]
    e=str(int(d)+int(c))
    print(e[::-1].lstrip('0'))
