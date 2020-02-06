def max_product_of_three(A):
    A.sort()

    # second option is for cases where one of the last 3 numbers is negative.
    # In that case two smallest negatives multiplied with last integer will result in a positive max
    return max(A[-3] * A[-2] * A[-1], A[0] * A[1] * A[-1])
