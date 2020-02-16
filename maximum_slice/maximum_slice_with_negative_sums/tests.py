from maximum_slice.maximum_slice_with_negative_sums.max_slice import max_slice

assert max_slice([-2, 1]) == 1
assert max_slice([-1, -2, 5, -3, 1, 2]) == 5
assert max_slice([-1, -2, 5, -2, 1, 2]) == 6
