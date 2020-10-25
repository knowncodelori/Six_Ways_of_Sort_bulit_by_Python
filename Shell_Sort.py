with open('test_in.txt') as fh: #打开未排序的数组文件，并将其转换为int型数组
    strnums = fh.read().split(",")
    nums = [int(num) for num in strnums]

def InsertionSort(ISnums: list()) -> list(): #因为希尔排序对每个序列片段需要用到直接插队排序，所以将之前写的插队排序改写成了一个函数放在这里
    ans = [ISnums[0]]
    for num in ISnums[1:]:
        n = len(ans)
        for id in range(n):
            if ans[id] > num: ans.insert(id, num)
        if n == len(ans): ans.append(num)
    return ans

n = len(nums)
step = n // 2
while step > 0:
    for first in range(step):
        temp = nums[first::step]
        temp = InsertionSort(temp)
        tempid = 0
        for id in range(first,n,step):
            nums[id] = temp[tempid]
            tempid += 1
    step =  step // 2
ans = nums

with open('sorted.txt','w') as ansfh: #将排序结果ans写入sorted文本文档中
    ansfh.write('Shell Sort:' + str(ans))