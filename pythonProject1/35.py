# 给的东西： 一个排序数组和一个目标值
# 要做什么操作：在数组中找到目标值，有就返回索引，没有的话就插入适合的位置
# 返回： 返回索引值

def search_insert_position (List: list, target: int) -> int:
    # 首先遍历这个数组
    # 遍历出来的数看看是不是等于target
    # 如果等于就返回索引
    # 如果target不在里面，就直接插入数组中
    for i in range(len(List)):
        if  List[i] == target:
            return i
    for j in range (len(List)):
        if List[0] >= target:
            List.insert(0,target)
            return 0
        elif List[-1] <= target:
            List.append(target)
            return len(List)-1
        elif List[j] < target < List[j+1]:
            List.insert(j+1, target)
            return j+1


def search_insert_position(nums: list, target: int) -> int:
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2  # 计算中间值

        if nums[mid] == target:  # 找到目标值
            return mid
        elif nums[mid] < target:  # 如果目标大于 mid 值，搜索右半部分
            left = mid + 1
        else:  # 如果目标小于 mid 值，搜索左半部分
            right = mid - 1

    # 如果没找到目标，返回插入位置
    return left  # `left` 会指向目标值应插入的位置

