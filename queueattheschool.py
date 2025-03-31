line= input().split()
n=int(line[0])
t=int(line[1])
line=input()
line=list(line)
for _ in range(t):
    i = 0
    while i < n - 1:
        if line[i] == 'B' and line[i + 1] == 'G':
            line[i], line[i + 1] = line[i + 1], line[i]
            i += 1
        i += 1
print("".join(line))
#266B