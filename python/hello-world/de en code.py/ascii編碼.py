print(chr(33))
#編碼轉文字

print(ord('!'))
#文字轉編碼

a="66 114".split(" ")
#字串的分割(用split裡的東西分割)


i = "66 114 101 97 107 65 76 76 67 84 70 123 65 109 118 48 117 68 121 101 114 118 80 116 109 86 114 57 83 83 83 75 125"
i_s = i.split(" ")
print (eval(i_s[2]))

for x in range(len(i_s)) :
    print(int(i_s[x]))

print("=================================")

for x in range(len(i_s)) :
    print(chr(int(i_s[x])))
