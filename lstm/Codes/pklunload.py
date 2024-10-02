import pickle
import os

ROOT = os.getcwd()
EX        = 'BTcP prediction'
EPOCHS  = 300
BATCHES = 100
IN_LENS = [120, 72, 24]
OUT_LEN = 24
TAUS    = [1,2,3,4,6,8,12]
DATA_DIR   = os.path.join(ROOT, 'Example datasets')
SAVE_DIR   = os.path.join(ROOT, 'Results')
WEIGHT_DIR = os.path.join(ROOT, 'Weights')

for IN_LEN in IN_LENS:
    # Load dataset according to input lengths
    with open(os.path.join(DATA_DIR, 'data for '+str(IN_LEN)+' hours.pickle'), 'rb') as f:
        data = pickle.load(f)