with open('test_in.txt') as fh: #打开未排序的数组文件，并将其转换为int型数组
    strnums = fh.read().split(",")
    nums = [int(num) for num in strnums]

def QuickSort(QSnums:list) -> list:
    if len(QSnums) <= 1:return QSnums
    flag = QSnums[0]
    left = []
    right = []
    for num in QSnums[1:]:
        if num < flag :left.append(num)
        else: right.append(num)
    return QuickSort(left) + [flag] + QuickSort(right)
ans = QuickSort(nums)

with open('sorted.txt','w') as ansfh: #将排序结果ans写入sorted文本文档中
    ansfh.write('Quick Sort:' + str(ans))