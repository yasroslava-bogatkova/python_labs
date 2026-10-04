# Л/Р -Коллекции и матрицы

## Задание 1:

### min_max

```python
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
```

Если список не пустой, то функция циклом находит наибольшее и наименьшее,выводит их кортежем; иначе выводит ошибку
![](/images/lab02/min_max.png)

### unique_sorted

```python
def unique_sorted(nums: list[float | int]) -> list[float | int]:
    unique=list(set(nums))
    for n in range(len(unique)):
        for m in range(n+1,len(unique)):
            if unique[m]<unique[n]:
                unique[n],unique[m]=unique[m],unique[n]
    return unique
```
Сначала функция убирает повторы созданием множества,затем сортирует-фиксирует элемент, сравнивает с последующими, меняя их мастами, если правый оказыввается меньше левого
![](/images/lab02/unique.png)

### flatten
```python
def flatten(mat: list[list | tuple]) -> list:
    res=[]
    for row in mat:
        if not isinstance(row,(list,tuple)):
            raise TypeError()

        res=res+list(row)
    return res
```
Функция проверяет является ли каждый элемент списком, затем обЪединяет их в один плоский список
![](/images/lab02/flatten.png)

## Задание 2
### transpose
```python
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
```
Если список не пустой, то функция сначала проверяет является ли матрица прямоугольной,затем создает строку для каждого столбца, в которую добавляет элементы соответсвующей строки с этим номером
![](/images/lab02/transpose.png)

## row_sums
```python
def row_sums(mat: list[list[float | int]]) -> list[float]:
    expected_length=len(mat[0])
    for row in mat:
        if len(row)!=expected_length:
            raise ValueError()
    return [sum(row) for row in mat]
```
Функция сначала проверяет прямоугольная ли матрица,затем генератором счиатает сумму каждой строки
![](/images/lab02/row_sum.png)

### col_sums
```python
def col_sums(mat: list[list[float | int]]) -> list[float]:
    mat1=transpose(mat)
    return row_sums(mat1)
```
Функция меняет строки и столбцы местами, использует предыдущую функцию для подсчета строк(бывших столбцов), где проверяется прямоугольная ли матрица
![](/images/lab02/col_sum.png)