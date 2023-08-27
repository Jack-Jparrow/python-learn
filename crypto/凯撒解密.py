'''
 * 凱撒解密
 *
 * @Author: Jack Jparrow 
 * @Date: 2021-05-09 09:50:51 
 * @Last Modified by: Jack Jparrow 
 * @Last Modified time: 2021-05-09 09:50:51 
'''
from string import ascii_uppercase

# Ciphertext = "QEB NRFZH YOLTK CLU GRJMP LSBO QEB IXWV ALD"
Ciphertext = "gmbh|egfcbggf~"

Ciphertext = Ciphertext.upper()

def shift(Key):
    Plaintext = ""

    for i in Ciphertext:
        if i not in ascii_uppercase:
            Plaintext += i
        else:
            Plaintext += chr(((ord(i)-ord("A")-Key) % 26)+ord("A"))

    return Plaintext

for Key in range(26):
    print(shift(Key))
