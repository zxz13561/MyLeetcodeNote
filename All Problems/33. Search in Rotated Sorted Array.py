class Solution(object):
    def search(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            result = {nums[left]: left, nums[right]: right, nums[mid]: mid}.get(target)
            if result is not None: return result
            if nums[left] < nums[mid]:
                if nums[left] < target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target < nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1


if __name__ == '__main__':
    run = Solution()
    print(run.search([4,5,6,7,0,1,2], 0))
