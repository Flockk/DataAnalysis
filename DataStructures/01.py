def check_brackets(s):
    stack = []
    for char in s:
        if char in ['{', '[', '(']:
            stack.append(char)
        elif char in ['}', ']', ')']:
            if not stack:
                return False
            if stack[-1] != '{' and char == '}':
                return False
            if stack[-1] != '[' and char == ']':
                return False
            if stack[-1] != '(' and char == ')':
                return False
            stack.pop()
    return not stack


sequence = input()
print("YES" if check_brackets(sequence) else "NO")