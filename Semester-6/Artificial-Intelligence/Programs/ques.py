n = int(input())
arr = []
for i in range(n):
    arr.append(input())
a=0
b=0
flag = False
for i in range(n):
    if arr[i]=='w':
        if not flag:
            flag = True
    else:
        if flag:
            a+=1
            flag = False

print(a)
        

