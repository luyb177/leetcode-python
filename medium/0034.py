"""
34 在排序数组中查找元素的第一个和最后一个位置

Key idea:
Finding the leftmost and rightmost boundaries both work by repeatedly using left and right to shrink the original array.
When searching for the leftmost boundary, it's right that ends up holding the answer; when searching for the rightmost boundary, it's left that holds the answer.
"""


class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        # Solve this problem using two binary searches:
        # one to find the left boundary and one to find the right boundary.
        leftBorder = self.getLeftBorder(nums, target)
        rightBorder = self.getRightBorder(nums, target)

        if leftBorder == -2 or rightBorder == -2:
            return [-1, -1]

        #
        if rightBorder - leftBorder > 1:
            return [leftBorder + 1, rightBorder - 1]

        # target is not present in the array. {1, 2 ,4} find 3
        return [-1, -1]

    # 5 7 7 8 8 10 find 8
    # 0 1 2 3 4  5 return 5
    def getRightBorder(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        rightBorder = -2

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid - 1
            else:
                # <= target
                left = mid + 1
                rightBorder = left

        return rightBorder

    # 5 7 7 8 8 10 find 8
    # 0 1 2 3 4  5 return 2
    def getLeftBorder(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        leftBorder = -2

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                # >= target
                right = mid - 1
                leftBorder = right

        return leftBorder

# 这种做法——找到一个target，向左向右扩展是不对的，有时间限制，
# class Solution:
#     def searchRange(self, nums: list[int], target: int) -> list[int]:
#         left = 0
#         right = len(nums) - 1
#
#         while left <= right:
#             mid = (left + right) // 2
#
#             if nums[mid] == target:
#                 # 向左、向右扩展
#                 left, right = mid, mid
#
#                 while left > 0:
#                     if nums[left - 1] == target:
#                         left -= 1
#                     else:
#                         break
#
#                 while right < len(nums) - 1:
#                     if nums[right + 1] == target:
#                         right += 1
#                     else:
#                         break
#
#                 return [left, right]
#
#             elif nums[mid] < target:
#                 left = mid + 1
#
#             else:
#                 right = mid - 1
#
#         return [-1, -1]