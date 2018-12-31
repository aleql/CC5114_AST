from Generator.TreeGenerator import TreeGenerator

terminals = [1, 2, 3, 'x', 'y', 'z']
height = 5
tg = TreeGenerator(terminals, height)

for i in range(10):
    tree = tg.generate_tree(tg.height)
    print(str(tree))

