from stacks_and_queues.brackets.brackets import brackets

assert brackets('') == 1
assert brackets('((()))()') == 1
assert brackets(')(') == 0
assert brackets('))((') == 0
assert brackets('((()))()()(()') == 0

assert brackets('[]') == 1
assert brackets('[)') == 0
assert brackets('[[]]') == 1
assert brackets('[({})]') == 1
assert brackets('[[]]{()}{}') == 1
