def number_of_disc_intersections(A):
    total = 0

    for i in range(len(A)):
        for j in range(i + 1, len(A)):
            if j - i <= A[i] + A[j]:
                total += 1
                if total == 10000000:
                    return -1
    return total
