n=int(input());arr=[int(i) for i in input().strip().split()];lst=[];t=n//3
for i in arr:
    if i in lst:
        continue
    if(arr.count(i)>t):
        lst.append(i)
if lst==[]:
    print(-1);exit()
print(*lst)
