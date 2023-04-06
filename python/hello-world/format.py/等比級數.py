r_s = input ("輸入公比:")
r = int(r_s)

a1_s = input ("輸入首項:")
a1 = int(a1_s)

n_s = input ("輸入項數:")
n = int(n_s)

def compute(r,a1,f):
    s = a1

    for i in range(f):
        an =  a1 * r**(i+1)
        s += an

    return s

print ("你的等比級數數列:")

for x in range(n):
    print (compute(r,a1,x) , end=",") 
    