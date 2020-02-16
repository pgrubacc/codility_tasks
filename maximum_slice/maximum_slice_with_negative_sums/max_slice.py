def max_slice(A):
    current_sum = 0
    best_sum = None
    for value in A:
        current_sum = max(max(float('-inf'), current_sum + value), value)
        best_sum = current_sum if best_sum is None else max(best_sum, current_sum)
    return best_sum
