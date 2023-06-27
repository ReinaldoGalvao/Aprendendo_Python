"""
i = 0
while i < 5:
    print(f'oi o i vale {i}')
    i += 1
"""

i = 0
while i < 10:
    print(i)
    if i % 2 == 1:
        i = i + 2
        continue
    i += 1