from maximum_slice.max_profit.max_profit import calculate_max_profit

assert calculate_max_profit([1, 2, 3, 4, 5]) == 4
assert calculate_max_profit([1, 2, 3, 0, 5]) == 5
assert calculate_max_profit([1, 1, 1, 0, 1, 1]) == 1
assert calculate_max_profit([2, 1, 1, 1]) == 0
assert calculate_max_profit([1]) == 0
assert calculate_max_profit([1, 100, 101, 102]) == 101
assert calculate_max_profit([23171, 21011, 21123, 21366, 21013, 21367]) == 356