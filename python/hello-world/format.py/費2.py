def feb(n):
    if n < 1:
        return 1
    else:
        return(feb(n-1)+feb(n-2))


print ("費式數列，是求出第N項的值！")
n_s = input ("輸入n:")
n = int(n_s)

for i in range(n):
    print (feb(i), end=",") 
    # 把結束從預設的"換行"改成","