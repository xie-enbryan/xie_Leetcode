# 输入：非递减顺序 排列的整数数组 nums1 和 nums2，另有两个整数 m 和 n
# 输出： 合并后的整数数组nums1

# 首先按照题意，演唱nums1的数组长度
# 遍历这个数组nums2， 因为它们两个都是非递增的，拿一个nums2的数据出来，就依次跟nums的相比，遇到合适的位置插进去， 最后就合并了

# 这种解法需要额外的空间，merge
def merge_two_dist (nums1: list[int], nums2: list[int], m: int, n: int) -> list[int]:
        merge = nums1[:m]+nums2
        merge.sort()

        nums1[:m+n] = merge


## 这种解法不需要额外的空间,
def update_merge_two_list (nums1: list[int], m: int, nums2: list[int], n: int) -> bool:
        p1 =  m-1 # p1指向nums1数组的非0数字的末尾
        p = m+n-1  # p指向nums1整个数组的末尾
        p2 = n-1 # 指向nums2数组的末尾

        # 用笔画一下，就知道这个逻辑是怎么运行的了，一边遍历nums2数组，然后与nums2做比较，决定nums2拿出来的数据是放在哪个合适的位置
        # 当我遍历完nums2
        while p2 >= 0:
                if p1 >=0 and nums1[p1] > nums2[p2]:
                        # 先把最大的给它挪到最后去先
                        nums1[p] = nums1 [p1]
                        p1 -= 1
                else:
                        nums1[p] = nums2 [p2]
                        p2 -= 1
                p -= 1





