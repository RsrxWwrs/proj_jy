def check_brackets(string):
    stack = []
    result = ''

    for char in string:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                result += '?'
        else:
            result += char

    for char in stack:
        result += 'x'

    return result


test_cases = [
    "bge)))))))))",
    "((IIII))))))))",
    "()()()()(uuu",
    "))))UUUU((()"
]

for test_case in test_cases:
    print(check_brackets(test_case))