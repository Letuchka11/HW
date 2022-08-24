def get_list() -> list:
    return list(range(0, 1000000, 2))


class Solution:
    def find_target(self, list, target):
        self.list = get_list()
        low = 0
        high = len(self.list)
        mid = int(high) // 2
        while True:
            if target == mid:
                return mid
            elif target > mid:
                low = mid
                mid = (low + high) // 2
                continue
            elif target < mid:
                high = mid
                mid = (low + high) // 2
                continue


print(Solution().find_target(get_list(), 435678))

# with open('binary_search.txt', 'x') as file:
#     pass