stack = []
min_values = []


def push_value(x):
    stack.append(x)
    if not min_values or x <= min_values[-1]:
        min_values.append(x)


def pop_value():
    if stack[-1] == min_values[-1]:
        min_values.pop()
    return stack.pop()


def min_value():
    return min_values[-1]


q = int(input())
results = []
for i in range(q):
    operation = input().split()
    if operation[0] == 'push':
        push_value(int(operation[1]))
    elif operation[0] == 'pop':
        pop_value()
    elif operation[0] == 'min':
        results.append(min_value())

for result in results:
    print(result)
