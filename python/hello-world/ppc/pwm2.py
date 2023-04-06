#!/usr/bin/env python3
from pwn import *

r = remote('120.114.62.205', 2401)
r.recvlines(8)

r.recvuntil('sentence : ')
x = r.recvline().strip().decode()
ans = x.lower().replace('-', ' ').replace('_', ' ')
print (ans)

print('================================================')
r.sendlineafter('answer : ', ans)

r.interactive()
