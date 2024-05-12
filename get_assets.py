#!python

import sys
from os import mkdir, chdir, system

def clone(repo):
	print("Cloning", repo)
	system("git clone " + repo)

remotes=[
	"https://github.com/ArsThaumaturgis/PandaSampleModels.git",
	"https://github.com/wezu/p3d_samples.git",
	"https://github.com/ArsThaumaturgis/Panda3DTutorial.io.git"
]

# Create an assets directory, avoid an overwrite
try:
    mkdir("assets");
except FileExistsError:
    print("Found existing assets directory. Avoiding overwrite.")
    sys.exit()

# Jump inside and grab the necessities
chdir("assets")

for r in remotes:
    clone(r)
