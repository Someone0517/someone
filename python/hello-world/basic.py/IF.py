mon = 10
day = 23
c = 0
for i in range(mon):
    if(i==0):
        continue
    if(i<=7):
        if(i%2==0 and i!=2):
            #偶數
            c+=30
        if(i%2==1):
            #奇數
            c+=31
        if(i==2):
            c+=29
    if(i>7):
        if(i%2==0 and i!=2):
            #偶數
            c+=31
        if(i%2==1):
            #奇數
            c+=30
c = c + day
print(c)
        
