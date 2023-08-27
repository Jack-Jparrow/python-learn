'''
Author: Jack Jparrow
Date: 2022-04-08 21:38:42
LastEditTime: 2022-04-08 21:56:54
LastEditors: Jack Jparrow
Description: 
'''

import base64

fake_box = "abcdefghijklmnABCDEFGHIJKLMNOPQRSTUVWXYZopqrstuvwxyz0123456789+/="  # 逆向发现的自定义的表
true_box = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/="
cipher = "FYHwNYHwQziwmdiyndm1RC=="  # 逆向到的密文
flag_base64 = ""

ciper_list = list(cipher)
for i in ciper_list:
    flag_base64 += true_box[fake_box.find(i)]

print("standard base64 code:", flag_base64)
print(base64.b64decode(flag_base64.encode()))
