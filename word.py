#59A
line=input()
x=sum(1 for c in line if c.isupper())
y=sum(1 for c in line if c.islower())
if y>=x:
    print(line.lower())
else:
    print(line.upper())