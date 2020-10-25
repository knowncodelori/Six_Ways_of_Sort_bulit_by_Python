with open('test_in.txt') as fh: #打开未排序的数组文件，并将其转换为int型数组
    strnums = fh.read().split(",")
    nums = [int(num) for num in strnums]

n = len(nums)
for i in range(n - 1):
    for j in range(1, n - i):
        if nums[j-1] > nums[j] : nums[j-1], nums[j] = nums[j], nums[j-1]
ans = nums

with open('sorted.txt','w') as ansfh: #将排序结果ans写入sorted文本文档中
    ansfh.write('Bubble Sort:' + str(ans))