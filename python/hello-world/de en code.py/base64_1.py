import base64
#去查 base64 base 32 in,de code 函式庫(注意import)

q_64 = "QnJlYWtBTExDVEZ7NTN1c1pRM2hXVzI1ZGNoWjdkWGV9"
x = base64.b64decode(q_64)
#解碼 decode
print(x)

q_32 = "IJZGKYLLIFGEYQ2UIZ5TS6BUHA2VMUZXO5UWS5CCLJMFKVLIJVSX2==="
y = base64.b32decode(q_32)
#解碼 decode
print(y)

print("==============================")

q ="BreakallCTF{happyhackinghighhaaha}"

b = q.encode('UTF-8')
#先變UTF-8 才能編碼<字串不行>

bytes_encode = base64.b64encode(b)
print(bytes_encode)