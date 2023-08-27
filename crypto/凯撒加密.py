'''
 * 凱撒加密
 *
 * @Author: Jack Jparrow 
 * @Date: 2021-05-09 09:12:46 
 * @Last Modified by: Jack Jparrow 
 * @Last Modified time: 2021-05-09 09:12:46 
'''

from string import ascii_uppercase

Plaintext = "THE QUICK BROWN F0X JUMPS OVER THE LAZY DOG"
Key=3
Plaintext = Plaintext.upper()
Ciphertext = ""

for i in Plaintext:
    if i not in ascii_uppercase:
        Ciphertext += i
    else:
        Ciphertext += chr(((ord(i)-ord("A")-Key) % 26)+ord("A"))

print (Ciphertext)
