with open('test_in.txt') as fh: #打开未排序的数组文件，并将其转换为int型数组
    strnums = fh.read().split(",")
    nums = [int(num) for num in strnums]

ans = [nums[0]]
for num in nums[1:]:
    n = len(ans)
    for id in range(n):
        if ans[id] > num: ans.insert(id,num)
    if n == len(ans): ans.append(num)


with open('sorted.txt','w') as ansfh: #将排序结果ans写入sorted文本文档中
    ansfh.write('Insertion Sort:' + str(ans))