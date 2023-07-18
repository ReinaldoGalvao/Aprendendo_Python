nums = [2, 7, 11, 15]
target = 9

complement_map = {}

for i, num in enumerate(nums):
    complement = target - num

    if complement in complement_map:
        print([complement_map[complement], i])
        quit()

    complement_map[num] = i

print([])
