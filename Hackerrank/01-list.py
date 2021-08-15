# link--> https://www.hackerrank.com/challenges/python-lists/problem

ls=[]
n=int(input())
while n:
    n-=1
    words=input().split()
    if words[0]=='insert':
        ls.insert(int(words[1]),int(words[2]))
    elif words[0]=='append':
        ls.append(int(words[1]))
    elif words[0]=='sort':
        ls.sort()
    elif words[0]=='remove':
        ls.remove(int(words[1]))
    elif words[0]=='pop':
        ls.pop()
    elif words[0]=='reverse':
        ls.reverse()
    elif words[0]=='print':
        print(ls)