from LLD2.Structural.Flyweight.TreeTexture import TreeTexture


class Tree:
    #with flyweight
    def __init__(self, x, y, tree_texture: TreeTexture ):
        self.x = x
        self.y = y
        self.tree_texture = tree_texture

#without flyweight
# def __init__(self, x, y, color,name, texture, image):
#     self.x = x
#     self.y = y
#     self.color = color
#     self.name = name
#     self.texture = texture
#     self.image = image

