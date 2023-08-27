'''
Author: Jack Jparrow
Date: 2022-03-27 19:18:07
LastEditTime: 2022-03-27 19:19:20
LastEditors: Jack Jparrow
Description: 
'''
f_list = r'''D:\VMware Share\Kali-KDE\逃离东南亚\日记3\source_code\elf\rtld.c
D:\VMware Share\Kali-KDE\逃离东南亚\日记3\source_code\malloc\arena.c
D:\VMware Share\Kali-KDE\逃离东南亚\日记3\source_code\malloc\malloc.c'''
f_list = f_list.split('\n')

result = ''

for f in f_list:
    for data in open(f, 'r').readlines():
        data = data[:-1]
        if '}' in data:
            data = data.split('}')[-1]
            if '\t' in data:
                data1 = data[::].replace('\t', '')
                data1 = data1.replace(' ', '')
                if not data1:
                    print([data])
                    result += data

result = result.replace('\t', '1')
result = result.replace(' ', '0')
print(result)