import pickle
import os

ROOT = r"/home/jaz/coding/BTcP-prediction-main/"
DATA_DIR   = os.path.join(ROOT, 'Example datasets')
IN_LENS = [120, 72, 24]
OUT_LEN = 24

for IN_LEN in IN_LENS:
    with open(os.path.join(DATA_DIR, 'data for '+str(IN_LEN)+' hours.pickle'), 'rb') as f:
            data = pickle.load(f)
            # visualize the data, it's dictionary
            
            for key in data.keys():
                print(key)
                print(data[key].shape)
                print(data[key])
                print()
            
            