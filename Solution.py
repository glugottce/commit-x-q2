n=int(input())
a=list(map(int,input().split()))
flag= int(n/3)
res=[]
new_flag=0
for i in a:
    va= a.count(i)
    if va>=flag:
        if i not in res:
            res.append(i)
        new_flag=1
if new_flag==0:
    print(-1)
else:
    print(*res)
