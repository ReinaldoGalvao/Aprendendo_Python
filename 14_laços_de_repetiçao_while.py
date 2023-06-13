i = 0
'''
while i < 10:
    print(i)
    if i >= 2:
        break
    i += 1
    
'''

while i < 10:
    print(i)
    if i % 2 == 1:
        i += 2
        continue
    i += 1