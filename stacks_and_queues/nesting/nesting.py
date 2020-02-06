def nesting(S):
    if len(S) % 2 == 1:
        return 0

    stack = []

    for el in S:
        if el == '(':
            stack.append(el)
        elif el == ')':
            try:
                stack.pop()
            except IndexError:
                return 0
        else:
            return 0

    if len(stack) != 0:
        return 0
    return 1
