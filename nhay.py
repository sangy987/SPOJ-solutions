# your code goes here
import re
def findall(needle, haystack):
    a= [m.start() for m in re.finditer('(?={0})'.format(re.escape(needle)), haystack)]
    return a
while True:
    try:
        n=int(input())
        ne=input()
        ha=input()
        k=findall(ne, ha)
        if len(k)==0:
            print('\n')
        else:
            for i in k:
                print(i)
    except EOFError:
        break
 
