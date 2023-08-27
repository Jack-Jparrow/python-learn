'''
Author: Jack Jparrow
Date: 2022-06-13 20:38:24
LastEditTime: 2022-06-14 08:53:31
LastEditors: Jack Jparrow
Description: 
'''
b = [3, 5, 2, 5, 5, 13, 13, 1, 13, 6, 7, 8, 8, 9, 9]

b.sort(reverse=True)        #用sort()函数将列表中的元素从大到小排序
for i in range(0, len(b)):
    print(b[i], end=' ')     #输出的数之间用空格隔开

print()

cur_index = 1
cur_grade = 0 
count = 1
print(f'1', end = ' ')
for i in range(1, len(b)):

    if b[i] == b[i - 1]:
        count += 1
        print(cur_index, end = ' ')
    else:
        cur_index += count
        print(cur_index, end = ' ')
        count = 1
