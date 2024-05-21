from typing import TextIO
from smd_structs import *

class SMDContext:

    def __init__(self):
        self.in_nodes = False
        self.in_skeleton = False

    def setNodes(self):
        self.in_nodes = True
        self.in_skeleton = False
    
    def setSkeleton(self):
        self.in_nodes = False
        self.in_skeleton = True

def parseSMD(stream: TextIO):

    context = SMDContext()

    smd_version : int
    bones : list[Bone] = []
    movements : list[Frame] = []

    for line in stream:

        if line.startswith('//'):
            continue

        tokens = line.split()

        if context.in_nodes:
            bones.append(Bone.load(tokens))
            continue

        if context.in_skeleton:
            movements.append(Movement.)

        if tokens[0] == 'version':
            smd_version = int(tokens[1])
            continue

        if tokens[0] == 'nodes':
            context.setNodes()
            continue

        if tokens[0] == 'skeleton':
            context.setSkeleton()
            continue