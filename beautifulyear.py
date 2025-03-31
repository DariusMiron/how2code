#271A
n=int(input())
if len(set(str(n))) == len(str(n)):
    n+=1
while len(set(str(n))) < len(str(n)):
    n+= 1
print(n)