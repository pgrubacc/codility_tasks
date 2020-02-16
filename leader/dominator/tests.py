from leader.dominator.dominator import dominator

assert dominator([1, 2, 2, 2, 2, 5]) == 4
assert dominator([1, 2, 3]) == -1
assert dominator([1, 1, 1, 1, 1]) == 4
assert dominator([1]) == 0
assert dominator([1, 1, 1, 3, 3, 3]) == -1
assert dominator([1, 1, 1, 3, 3, 3, 3]) == 6
