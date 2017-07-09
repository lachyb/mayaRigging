"""
Created following Drhuv
"""

from maya import cmds

def createGear(teeth=10, length=0.3):
    spans = teeth * 2
    cmds.polyPipe(subdivisionsAxis=spans)