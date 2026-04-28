t = int(input())

for i in range(t):
    inp = str(input())
    if(inp[0] == "0"):
        tot = 0
    else:
        if inp[0] == "?":
            tot = 9
        else: 
            tot = 1
        for j in range(1,len(inp)):
            if inp[j] == "?":
                tot *= 10
    print(tot)
