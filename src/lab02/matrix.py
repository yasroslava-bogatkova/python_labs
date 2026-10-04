def transpose(mat: list[list[float | int]]) -> list[list]:
    if not mat:
        return []
    expected_length=len(mat[0])
    for row in mat:
        if len(row)!=expected_length:
            raise ValueError()
    result=[]
    for c_index in range(expected_length):
        new_row=[]
        for row in mat:
            new_row.append(row[c_index])
        result.append(new_row)
    return result


def row_sums(mat: list[list[float | int]]) -> list[float]:
    expected_length=len(mat[0])
    for row in mat:
        if len(row)!=expected_length:
            raise ValueError()
    return [sum(row) for row in mat]

def col_sums(mat: list[list[float | int]]) -> list[float]:
    mat1=transpose(mat)
    return row_sums(mat1)

test_case_transpose=[[[1,2,3]],[[1],[2],[3]],[[1,2],[3,4]],[],[[1,2],[3]]]
print('transpose:')
for case in test_case_transpose:
    try:
        result=transpose(case)
        print(f'{case} -> {result}')
    except ValueError:
        print(f'{case} -> Матрица должна быть прямоугольной')

test_case_rowsum=[[[1, 2, 3], [4, 5, 6]], [[-1,1],[10,-10]],[[0,0],[0,0]],[[1,2],[3]]]
print('row_sum:')
for case in test_case_rowsum:
    try:
        result=row_sums(case)
        print(f'{case} -> {result}')
    except ValueError:
        print(f'{case} -> Матрица должна быть прямоугольной')

test_case_colsum=[[[1,2,3],[4,5,6]], [[-1,1],[10,-10]], [[0,0],[0,0]], [[1,2],[3]]]
print('col_sum:')
for case in test_case_colsum:
    try:
        result=col_sums(case)
        print(f'{case} -> {result}')
    except ValueError:
        print(f'{case} -> Матрица должна быть прямоугольной')
