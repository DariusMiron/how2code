#281A
w=input()
n=w
if w[0].isupper():
    print(w)
else:
    n=n[0].upper()
    print(n+w[1:])