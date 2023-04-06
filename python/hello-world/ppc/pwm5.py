#!/usr/bin/env python3
from pwn import *
import string

r = remote('120.114.62.205', 2407)

r.recvlines(8)

for _ in range(100):
    r.recvuntil(b'money : ')
    money = int(r.recvline().strip())
    r.recvuntil(b'interest : ')
    interest = int(r.recvline().strip().strip(b'%'))
    r.sendlineafter('answer : ', str(money + money // 100 * interest))

r.interactive()