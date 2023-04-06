def function(m, n):
    while (m!=0):

        if (n==0):
            n = 1

        else:
            n= function(m,n-1)

        m = m-1
    return n+1

print(function(2,2))
