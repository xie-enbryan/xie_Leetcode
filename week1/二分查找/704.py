# 输入： n 个元素有序的（升序）整型数组 nums 和一个目标值 target
# 输出： 返回target值在整型数组中的下标，否则返回-1
# 操作： 搜索 nums 中的 target

# 直接用二分查找，从两边开始查找起来，判断是不是等于target，等于就返回下标
# 当left>right 就表示遍历完了，还没有找到，就返回-1

def binary_search (nums: list[int], target: int) -> int:
    left, right = 0, len(nums)-1

    while left <= right: # = 表示当剩最后一个元素时，恰好target就是最后一个元素
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid+1
        elif nums[mid] > target:
            right = mid-1
        else:
            return mid

    return -1



