def function(n):
    s = 0

    for x in range(1+n):
     s += x

    return s 
    """
    這個 function 是公差為一的等差級數。
    """

i = input("給我資料 : ")
i_i = int(i)

print(function(i_i))