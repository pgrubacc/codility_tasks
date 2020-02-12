from stacks_and_queues.fish.fish import fish

assert fish([4, 3, 2, 1, 5], [0, 1, 0, 0, 0]) == 2
assert fish([1, 2, 3], [0, 0, 0]) == 3
assert fish([1, 2, 3, 4], [1, 0, 0, 0]) == 3
assert fish([4, 3, 2, 1], [1, 0, 0, 0]) == 1
assert fish([4, 3, 10, 5], [1, 0, 1, 0]) == 2
assert fish([0, 3, 2, 5, 4], [0, 1, 0, 1, 0]) == 3
assert fish([90, 1, 2, 3, 4, 5], [1, 0, 0, 0, 0, 0]) == 1
assert fish([100, 90, 80, 70, 60], [0, 0, 0, 0, 1]) == 5
assert fish([1, 2], [0, 1]) == 2
assert fish([99, 98, 92, 91, 93], [1, 1, 1, 1, 0]) == 2