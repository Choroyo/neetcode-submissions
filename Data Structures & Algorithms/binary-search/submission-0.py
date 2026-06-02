def binarySearch(target, start, end, nums) -> int:
    if start > end:
        return -1
    
    mid = (start + end) // 2
    if nums[mid] == target:
        return mid
    if nums[mid] < target:
        binarySearch(target, mid + 1, end, nums)
    if nums[mid] > target:
        binarySearch(target, start, mid - 1, nums)
    


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums)

        result = binarySearch(target, start, end, nums )
        if result == None:
            return -1
        return result