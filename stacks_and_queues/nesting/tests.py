from stacks_and_queues.nesting.nesting import nesting

assert nesting('') == 1
assert nesting('((()))()') == 1
assert nesting(')(') == 0
assert nesting('))((') == 0
assert nesting('((()))()()(()') == 0
