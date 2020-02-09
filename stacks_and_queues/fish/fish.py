def fish(A, B):
    i = 0

    fish_stack = []
    downstream_stack = []

    while i < len(A):
        if not fish_stack:
            if B[i] == 1:
                downstream_stack.append(i)
            fish_stack.append(i)
            i += 1
            continue
        if B[i] == 1:
            fish_stack.append(i)
            downstream_stack.append(i)
            i += 1
        else:
            last_fish_index = fish_stack[-1]
            if B[last_fish_index] == 1:
                if A[i] < A[last_fish_index]:
                    i += 1
                    continue
                else:
                    fish_stack.pop()
                    downstream_stack.pop()
                    if not downstream_stack:
                        fish_stack.append(i)
                        i += 1
                        continue
            else:
                fish_stack.append(i)
                i += 1

    return len(fish_stack)
