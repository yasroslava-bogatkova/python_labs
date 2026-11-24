def linear_search(nums: list, x) -> int:
    for i, val in enumerate(nums):
        if val == x:
            return i
    return -1


def binary_search(sorted_nums: list, x) -> int:
    lo = 0
    hi = len(sorted_nums) - 1

    while lo <= hi:
        mid = (lo + hi) // 2
        if sorted_nums[mid] == x:
            return mid
        elif sorted_nums[mid] < x:
            lo = mid + 1
        else:
            hi = mid - 1

    return -1


def two_sum_brute(nums: list[int], target: int) -> tuple[int, int] | None:

    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return (i, j)
    return None


def two_sum_fast(nums: list[int], target: int) -> tuple[int, int] | None:
    """То же, что two_sum_brute, но за один проход со словарём."""
    seen = {}  
    for i, x in enumerate(nums):
        need = target - x
        if need in seen:
            return (seen[need], i)
        seen[x] = i
    return None
