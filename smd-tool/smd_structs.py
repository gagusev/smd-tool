class Position:

    def __init__(self, x: float, y: float, z: float):
        self.x = x
        self.y = y
        self.z = z

class Rotation:

    def __init__(self, x: float, y: float, z: float):
        self.x = x
        self.y = y
        self.z = z

class Bone:

    def __init__(self, id: int, name: str, parent_id: int):
        self.id = id
        self.name = name
        self.parent_id = parent_id

    @classmethod
    def load(cls, tokens: list[str]):
        return cls(int(tokens[0]), tokens[1], int(tokens[2]))

class Movement:

    def __init__(self, bone: Bone, position: Position, rotation: Rotation):
        self.bone = bone
        self.position = position
        self.rotation = rotation

    @classmethod
    def load(cls, tokens: list[str]):
        return cls()

class Frame:

    def __init__(self, time: int, movements: list[Movement]):
        self.time = time
        self.movements = movements

class SMD:

    def __init__(self, version: int, nodes: list[Bone], skeleton: list[Frame]):
        self.version = version
        self.nodes = nodes
        self.skeleton = skeleton