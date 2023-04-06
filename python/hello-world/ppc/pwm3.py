#!/usr/bin/env python3
from pwn import *

r = remote('120.114.62.205', 2402)

r.recvlines(9)

for i in range(100):
    r.recvuntil('year : ')
    year = int(r.recvline().strip().decode())
    
    if ((year%400==0) or (year%4==0 and year%100!=0)):
        ans = 1
    else:
        ans = 0
        
    r.sendlineafter('answer : ', ["ordinary", "leap"][ans])

r.interactive()