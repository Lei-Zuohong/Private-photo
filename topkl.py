import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import pickle
import sys

infile = sys.argv[1]
outfile = sys.argv[2]

lena = mpimg.imread(infile)
with open(outfile, 'wb') as outfile:
    pickle.dump(lena, outfile)
