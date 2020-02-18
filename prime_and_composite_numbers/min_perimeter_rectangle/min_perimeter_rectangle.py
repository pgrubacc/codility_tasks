def min_perimeter_rectangle(A):
    i = 1

    last_divisor = 1
    while i*i <= A:
        if A % i == 0:
            last_divisor = i
        i += 1

    if last_divisor == 1:
        return 2*(A+1)
    other_divisor = A // last_divisor
    return 2*(last_divisor + other_divisor)
