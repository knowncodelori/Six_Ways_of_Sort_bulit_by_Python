with open('test_in.txt') as fh: #打开未排序的数组文件，并将其转换为int型数组
    strnums = fh.read().split(",")
    nums = [int(num) for num in strnums]

ans = []
while nums:
    minnum = min(nums)
    ans.append(minnum)
    nums.remove(minnum)

with open('sorted.txt', 'w') as ansfh:  # 将排序结果ans写入sorted文本文档中
    ansfh.write('Selection Sort:' + str(ans))