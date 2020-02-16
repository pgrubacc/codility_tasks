def max_subarray(numbers):
    best_sum = None  # or: float('-inf')
    current_sum = 0
    for x in numbers:

        current_sum = max(0, current_sum + x)

        best_sum = max(best_sum, current_sum)

    return best_sum


assert (max_subarray([-1, 0, 3, -2, 5, 6])) == 12
assert (max_subarray([-1, 0, 3, -4, 5, 6])) == 12
