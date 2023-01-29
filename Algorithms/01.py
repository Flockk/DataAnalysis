def binary_search(arr, x):
    left = 0
    right = len(arr) - 1
    # инициализируем левую и правую границы для поиска
    while left <= right:
        mid = int(left + (right - left) / 2)
        if arr[mid] <= x:
            left = mid + 1
        else:
            right = mid - 1
    # возвращаем индекс элемента, который больше x
    return left


n = int(input())
n_arr = list(map(int, input().split()))

m = int(input())
m_arr = list(map(int, input().split()))

for i in m_arr:
    result = len(n_arr) - binary_search(n_arr, i)
    print(result)