n = int(input())
a = list(map(int, input().split()))

min_index = a.index(min(a))
max_index = a.index(max(a))

if min_index < max_index:
    print(max_index - min_index - 1)
else:
    print(min_index - max_index - 1)