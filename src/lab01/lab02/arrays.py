def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    if not nums:
        raise ValueError()

    mini=nums[0]
    maxi=nums[0]
    for n in nums:
        if n>maxi:
            maxi=n
        elif n<mini:
            mini=n
    return mini,maxi

def unique_sorted(nums: list[float | int]) -> list[float | int]:
    unique=list(set(nums))
    for n in range(len(unique)):
        for m in range(n+1,len(unique)):
            if unique[m]<unique[n]:
                unique[n],unique[m]=unique[m],unique[n]
    return unique

def flatten(mat: list[list | tuple]) -> list:
    res=[]
    for row in mat:
        if not isinstance(row,(list,tuple)):
            raise TypeError()

        res=res+list(row)
    return res

test_cases_minmax=[[3,-1,5,5,0],[42],[-5,-2,-9],[],[1.5,2,2.0,-3.1]]
print('min_max:')
for case in test_cases_minmax:
    try:
        result=min_max(case)
        print(f'{case} -> {result}')
    except ValueError:
        print(f'{case} -> Список не должен быть пустым')

test_cases_unique=[[3,1,2,1,3],[],[-1,-1,0,2,2],[1.0,1,2.5,2.5,0]]
print('unique_sorted:')
for case in test_cases_unique:
    result=unique_sorted(case)
    print(f'{case} -> {result}')

test_cases_flatten=[ [[1,2],[3,4]], [[1,2],(3,4,5)], [[1],[],[2,3]], [[1,2],"ab"]] 
print("flatten:")
for case in test_cases_flatten:
    try:
        result=flatten(case)
        print(f'{case} -> {result}')
    except TypeError:
        print(f'{case} ->Все элементы должны быть списками или кортежами')
    