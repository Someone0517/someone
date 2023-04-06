c = 0
for h in range(6):
    for t in range(6):
        if(h==t):
            continue
        else:
            for n in range(6):
                if(n==h or n==t):
                    continue
                else:
                    c+=(h+1)*100+(t+1)*10+n+1


print(c)