n = input()
i = 0
result = ""
while i < len(n):
    if n[i] == '.':
        result += "0"
        i += 1
    elif i + 1 < len(n) and n[i:i+2] == '-.':
        result += "1"
        i += 2
    elif i + 1 < len(n) and n[i:i+2] == '--':
        result += "2"
        i += 2
print(result)
#32B