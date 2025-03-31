#69A
n=int(input())
x,y,z=0,0,0
for _ in range(n):
    line=input().split()
    a=int(line[0])
    b=int(line[1])
    c=int(line[2])
    x+=a
    y+=b
    z+=c
if x==0 and y==0 and z==0:
    print("YES")
else:
    print("NO")