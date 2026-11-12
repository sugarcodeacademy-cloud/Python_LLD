from LLD2.Structural.Flyweight.TreeTextureType import TreeTextureType
from LLD2.Structural.Flyweight.TreeTexture import TreeTexture


class TreeTypeFactory:
    CACHE = {}

    @staticmethod
    def get_tree_type(tree_type):
        if tree_type in TreeTypeFactory.CACHE:
            return TreeTypeFactory.CACHE[tree_type]
        tree_texture = TreeTypeFactory.create_tree_type(tree_type)
        TreeTypeFactory.CACHE[tree_type] = tree_texture
        return tree_texture

    @staticmethod
    def create_tree_type(tree_type):
        if tree_type == TreeTextureType.OAK:
            return TreeTexture("Green", "Oak","rough", bytearray(1024),False)
        elif tree_type == TreeTextureType.MAPLE:
            return TreeTexture("Red", "Maple", "smooth", bytearray(1024),True)
        elif tree_type == TreeTextureType.PINE:
            return TreeTexture("Green", "Pine", "conical", bytearray(1024), False)
