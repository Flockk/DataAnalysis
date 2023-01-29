n, k = map(int, input().split())
heights = list(map(int, input().split()))
queries = list(map(int, input().split()))

for q in queries:
    left = 0
    right = n - 1
    while left <= right:
        mid = int(left + (right - left) / 2)
        if heights[mid] < q:
            left = mid + 1
        else:
            right = mid - 1
    print(left)