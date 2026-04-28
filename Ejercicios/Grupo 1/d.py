s = "codeforces"
t = int(input())

for i in range(t):
    p = input()
    count = 0
    for j in range(10):
        if s[j] == p[j]:
            count += 1    
    print(count)


    