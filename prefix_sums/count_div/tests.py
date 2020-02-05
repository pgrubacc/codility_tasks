from prefix_sums.count_div.count_div import count_div

assert count_div(1, 5, 5) == 1
assert count_div(0, 5, 5) == 2
assert count_div(0, 100, 3) == 34
assert count_div(0, 101, 3) == 34
assert count_div(1, 100, 3) == 33
assert count_div(0, 99, 3) == 34
assert count_div(1, 99, 3) == 33
assert count_div(2, 98, 3) == 32
assert count_div(3, 98, 3) == 32
assert count_div(4, 98, 3) == 31
assert count_div(0, 0, 1) == 1
assert count_div(1, 1, 2) == 0
assert count_div(1, 0, 1) == 0
