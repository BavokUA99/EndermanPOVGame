from panda3d.core import loadPrcFile
loadPrcFile('configs.prc') 

# world generation
SEED = 5654947964
SCALE = 1.9

CHUNK_WIDTH = 16
terrain_width = 2 # max size for chunk list

# moving
MOVESPEED = 0.1
VECTORLIMIT = 2
VECTORSPEED = 0.0015