def equi_leader(A):
    leader = goldenLeader(A)
    if leader == -1:
        return 0

    subarray_counts = count_number_occurrences_in_subarrays(A, leader)
    equi_leaders = 0

    for i in range(1, len(A)):
        left_side_occurrences = subarray_counts[i-1]
        right_side_occurrences = subarray_counts[-1] - left_side_occurrences

        left_is_leader = True if left_side_occurrences > i // 2 else False
        right_is_leader = True if right_side_occurrences > (len(A)-i) // 2 else False

        if left_is_leader and right_is_leader:
            equi_leaders += 1

    return equi_leaders


def count_number_occurrences_in_subarrays(A, number):
    subarrays_counts = []
    occurrences = 0

    for i in range(len(A)):
        if A[i] == number:
            occurrences += 1
        subarrays_counts.append(occurrences)
    return subarrays_counts


def goldenLeader(A):
    n = len(A)
    size = 0
    for k in range(n):
        if size == 0:
            size += 1
            value = A[k]
        else:
            if value != A[k]:
                size -= 1
            else:
                size += 1
    candidate = -1
    if size > 0:
        candidate = value
    leader = -1
    count = 0
    for k in range(n):
        if A[k] == candidate:
            count += 1
    if count > n // 2:
        leader = candidate
    return leader
