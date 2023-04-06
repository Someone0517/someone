#!/usr/bin/env python3
from pwn import *
from fractions import Fraction

r = remote("120.114.62.205", 5127)

r.recvlines(5)

for _ in range(100):
    r.recvuntil("Fahrenheit : ")
    F = Fraction(int(r.recvline().strip()), 1)
    C = (F - 32) * 5 / 9
    r.sendline(str(C.numerator) + '/' + str(C.denominator))
    # numerator分子 denominator分母

r.interactive()