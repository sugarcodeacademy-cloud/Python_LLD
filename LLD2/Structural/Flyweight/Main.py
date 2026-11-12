from LLD2.Structural.Flyweight.TreeTextureType import TreeTextureType
from LLD2.Structural.Flyweight.TreeTypeFactory import TreeTypeFactory
from LLD2.Structural.Flyweight.Tree import Tree
from LLD2.Structural.Flyweight.TreeTexture import TreeTexture

#Without flyweight
# tree1: Tree = Tree(150, 200, "Green", "Oak", "Rough", bytearray(1024))
# tree2: Tree = Tree(250, 300, "Green", "Oak", "Rough", bytearray(1024))
# tree3: Tree = Tree(350, 200, "Green", "Oak", "Rough", bytearray(1024))
# tree4: Tree = Tree(450, 400, "Green", "Oak", "Rough", bytearray(1024))
# tree5: Tree = Tree(550, 500, "Green", "Oak", "Rough", bytearray(1024))
#
# print(tree1)
# print(tree2)

#With FlyWeight but without Factory
# oakTree: TreeTexture = TreeTexture("Green", "Oak","rough", bytearray(1024))
#
# tree1: Tree = Tree(150, 150, oakTree)
# tree2: Tree = Tree(250, 350, oakTree)
# tree3: Tree = Tree(450, 450, oakTree)
# tree4: Tree = Tree(550, 150, oakTree)
# tree5: Tree = Tree(250, 250, oakTree)
#
# print(tree1)

#With FlyWeight but with Factory
oak_tree = TreeTypeFactory.get_tree_type(TreeTextureType.OAK)
maple_tree = TreeTypeFactory.get_tree_type(TreeTextureType.MAPLE)
pine_tree = TreeTypeFactory.get_tree_type(TreeTextureType.PINE)

tree1: Tree = Tree(150, 150,oak_tree  )
tree2: Tree = Tree(250, 350,maple_tree )
tree3: Tree = Tree(450, 450, maple_tree)
tree4: Tree = Tree(550, 150, pine_tree)
tree5: Tree = Tree(250, 250, maple_tree)

print(tree1)