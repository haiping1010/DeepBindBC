import os
import re
from chimera import runCommand as rc # use 'rc' as shorthand for runCommand
from chimera import replyobj # for emitting status messages
###chimera --nogui ligprep.py
# change to folder with data files
os.chdir("/")

# gather the names of .pdb files in the folder
file_names = [fn for fn in os.listdir(".") if fn.endswith(".pdb")]

# loop through the files, opening, processing, and closing each in turn
for fn in file_names:
	replyobj.status("Processing " + fn) # show what file we're working on
	rc("open " + fn)
	rc("delete ligand") # put ligand in front of remainder of molecule
	# save image to a file that ends in .png rather than .pdb
         
        strinfo = re.compile('.pdb')
	fnx = strinfo.sub('_v.pdb',fn)
	#rc("write format pdb 0 "+ fn+".pdb")
        rc("write format pdb 0 " + fnx)

	rc("close all")
# uncommenting the line below will cause Chimera to exit when the script is done
#rc("stop now")
# note that indentation is significant in Python; the fact that
# the above command is exdented means that it is executed after
# the loop completes, whereas the indented commands that 
# preceded it are executed as part of the loop.
