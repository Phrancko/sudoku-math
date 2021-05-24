import pickle
import sys

from sums import *

if __name__ == "__main__":
    if len(sys.argv) > 1:
        filename = sys.argv[1]+'.pkl'
    else:
        filename = 'all_sums.pkl'

    dict = create_all_dicts()

    f = open(filename,"wb")
    pickle.dump(dict,f)
    f.close()
