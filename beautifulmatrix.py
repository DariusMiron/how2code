m=[]
for _ in range(5):
    line=input().split()
    m.append(line)
for i in range(5):
    for j in range(5):
        if m[i][j]=='1':
            print(abs(2-i) + abs(2-j))
#263A