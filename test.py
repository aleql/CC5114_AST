import itertools
import random

from AST.OpTree import OpTree
from Generator.TreeGenerator import TreeGenerator

terminals = [1, 2, 3, 'x', 'y', 'z']
height = 5
tg = TreeGenerator(terminals, height, random.Random(5))

env = {
    'x': 10,
    'y': -6,
    'z': 10
}

nodeA = tg.generate_tree(tg.height)
nodeB = tg.generate_tree(tg.height)

# Create new tree, as the best combination of the individuals
# Generate all combinations between two nodes and operations
combinations = [tg.operations, nodeA.toList(), nodeB.toList()]
combinations_perm = [tg.operations, nodeB.toList(), nodeA.toList()]
combinations = itertools.product(*combinations)
combinations_perm = itertools.product(*combinations_perm)

combinations = itertools.chain(combinations, combinations_perm)

# Find the best combination
best_tree = None
best_score = None
for combination in combinations:
    candidate_tree = OpTree(combination[0], combination[1], combination[2])
    candidate_score = candidate_tree.eval(env)

    # New best candidate
    if best_score is None or candidate_score > best_score:
        best_score = candidate_score
        best_tree = candidate_tree

# Mutate based of mutation_rate
best_tree = tg.mutate_tree(best_tree, 0.2)

copy_tree = best_tree.copy()

print(str(best_tree))
print(str(copy_tree))
