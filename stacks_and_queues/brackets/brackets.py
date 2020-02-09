def brackets(S):
    if len(S) % 2 == 1:
        return 0

    stack = []
    pushed_brackets = []
    brackets = {')': '(',
                ']': '[',
                '}': '{'}

    for el in S:
        if el in brackets.values():
            stack.append(el)
            pushed_brackets.append(el)
        else:
            if not pushed_brackets or el not in brackets.keys():
                return 0

            if pushed_brackets[-1] != brackets[el]:
                return 0

            try:
                stack.pop()
                pushed_brackets.pop()
            except IndexError:
                return 0

    if len(stack) != 0:
        return 0
    return 1
