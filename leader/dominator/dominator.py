def dominator(A):

    leader_stack = []

    for i in range(len(A)):
        if not leader_stack:
            leader_stack.append(A[i])
            continue
        if A[i] != leader_stack[-1]:
            leader_stack.pop()
            continue
        leader_stack.append(A[i])

    candidate = -1
    if leader_stack:
        candidate = leader_stack[0]

    candidate_count = 0
    index = 0

    for i in range(len(A)):
        if A[i] == candidate:
            candidate_count += 1
            index = i

    return index if candidate_count > len(A) // 2 else -1
