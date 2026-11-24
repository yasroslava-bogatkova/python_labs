import random
from src.lab07.sorting import bubble_sort, insertion_sort, selection_sort
from src.lab07.search import (
    linear_search,
    binary_search,
    two_sum_brute,
    two_sum_fast,
)


def check_sorting(fn, trials=100):
    for _ in range(trials):
        n = random.randint(0, 50)
        nums = [random.randint(-100, 100) for _ in range(n)]
        original = list(nums)
        result = fn(nums)
        assert result == sorted(nums), f"{fn.__name__} ошиблась на {nums}: {result}"
        assert nums == original, f"{fn.__name__} изменила исходный список"


def check_search(trials=100):
    assert linear_search([], 5) == -1
    assert binary_search([], 5) == -1
    assert binary_search([5], 5) == 0
    assert binary_search([5], 1) == -1

    for _ in range(trials):
        n = random.randint(0, 50)
        nums = [random.randint(-50, 50) for _ in range(n)]
        targets = [random.randint(-60, 60)]
        if nums:
            targets.extend([nums[0], nums[-1], random.choice(nums)])

        sorted_nums = sorted(nums)

        for x in targets:
            expected_lin = nums.index(x) if x in nums else -1
            got_lin = linear_search(nums, x)
            assert got_lin == expected_lin, (
                f"linear_search({nums}, {x}) -> {got_lin}, ожидалось {expected_lin}"
            )

            got_bin = binary_search(sorted_nums, x)
            if x in sorted_nums:
                assert 0 <= got_bin < len(sorted_nums) and sorted_nums[got_bin] == x, (
                    f"binary_search({sorted_nums}, {x}) -> {got_bin}"
                )
            else:
                assert got_bin == -1, (
                    f"binary_search({sorted_nums}, {x}) -> {got_bin}, ожидалось -1"
                )


def check_two_sum(trials=100):
    for _ in range(trials):
        n = random.randint(0, 40)
        nums = [random.randint(-50, 50) for _ in range(n)]

        if n >= 2 and random.random() < 0.5:
            i, j = random.sample(range(n), 2)
            target = nums[i] + nums[j]
        else:
            target = random.randint(-100, 100)

        res_brute = two_sum_brute(nums, target)
        res_fast = two_sum_fast(nums, target)

        if res_brute is None:
            assert res_fast is None, (
                f"Расхождение на {nums}, target={target}: brute=None, fast={res_fast}"
            )
        else:
            assert res_fast is not None, (
                f"Расхождение на {nums}, target={target}: brute={res_brute}, fast=None"
            )
            i, j = res_fast
            assert 0 <= i < j < n and nums[i] + nums[j] == target, (
                f"two_sum_fast вернул неверную пару {res_fast} на {nums}, target={target}"
            )


if __name__ == "__main__":
    random.seed(42)
    for fn in (bubble_sort, insertion_sort, selection_sort):
        check_sorting(fn)
    check_search()
    check_two_sum()
    print("OK")
