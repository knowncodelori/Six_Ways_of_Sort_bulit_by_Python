with open('test_in.txt') as fh: #打开未排序的数组文件，并将其转换为int型数组
    strnums = fh.read().split(",")
    nums = [int(num) for num in strnums]

def TwoMerge(MSnums1:list, Msnums2:list) -> list: #将两个有序数组合并成一个有序数组的函数
    ans = []
    cur1 = cur2 = 0
    while cur1 < len(MSnums1) and cur2 < len(Msnums2) :
        if MSnums1[cur1] <= Msnums2[cur2]:
            ans.append(MSnums1[cur1])
            cur1 += 1
        else:
            ans.append(Msnums2[cur2])
            cur2 += 1
    if cur1 < len(MSnums1): ans.extend(MSnums1[cur1:])
    else: ans.extend(Msnums2[cur2:])
    return ans

def MergeSort(MSnums:list) -> list:
    n = len(MSnums)
    if n == 1:
        return MSnums
    if n == 2:
        if MSnums[0] > MSnums[1]:
            MSnums[0], MSnums[1] = MSnums[1], MSnums[0]
        return MSnums
    return TwoMerge(MergeSort(MSnums[:n // 2]), MergeSort(MSnums[n // 2:]))
ans = MergeSort(nums)

with open('sorted.txt','w') as ansfh: #将排序结果ans写入sorted文本文档中
    ansfh.write('Merge Sort:' + str(ans))