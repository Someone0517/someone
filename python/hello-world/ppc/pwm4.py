#!/usr/bin/env python3
from pwn import *

r = remote('120.114.62.205', 2403)

for i in range(100):
    r.sendline(str(i+1))

r.interactive()