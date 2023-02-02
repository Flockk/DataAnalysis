def decode_string(string):
    stack = []
    for char in string:
        if not stack or stack[-1] != char:
            stack.append(char)
        else:
            stack.pop()
    return ''.join(stack)


encrypted_string = input()
print(decode_string(encrypted_string))
