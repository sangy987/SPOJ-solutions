# your code goes here
import re
 
 
def findall(needle, haystack):
    a= [m.start() for m in re.finditer('(?={0})'.format(re.escape(needle)), haystack)]
    return a
 
for _ in range(int(input())):
    a=input().split()
    p=a[1]
    s=a[0]
 
    k=findall(p, s)
 
    if len(k)==0:
        print('Not Found \n')
        
    else:
        print(len(k))
        for i in k:
            print(i+1, end=' ')
        print('\n'
