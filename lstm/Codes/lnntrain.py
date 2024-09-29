# Import custom LNN model
from Models import LNN_Model
import os, sys, pickle

# Set hyper parameters
EX        = 'BTcP prediction'
EPOCHS  = 300
BATCHES = 100
IN_LENS = [120, 72, 24]
OUT_LEN = 24
TAUS    = [1,2,3,4,6,8,12]


# Directories
DATA_DIR   = os.path.join(ROOT, 'Example datasets')
SAVE_DIR   = os.path.join(ROOT, 'Results')
WEIGHT_DIR = os.path.join(ROOT, 'Weights')
makedirs(SAVE_DIR)
makedirs(WEIGHT_DIR)

# Loop for training and testing
for IN_LEN in IN_LENS:
    with open(os.path.join(DATA_DIR, 'data for '+str(IN_LEN)+' hours.pickle'), 'rb') as f:
        data = pickle.load(f)

    for t in TAUS:
        # Data preparation steps (train, val, test split)
        trainX, trainY = split_XY(train, IN_LEN//t)
        testX_, testY = split_XY(test, IN_LEN//t)
        valX, valY = split_XY(val, IN_LEN//t)

        # Transformation (e.g., Reshape input data for LTC)
        trainX, valX, testX = transformation(trainX, valX, testX_, t)

        # Make Y as Binary score
        trainY_binary, valY_binary, testY_binary = make_binary_score_for_all(trainY, valY, testY)

        # Create the LNN model
        full_name = '_'.join([str(IN_LEN), str(OUT_LEN), 'LNN', str(t)])
        model = LNN_Model(trainX.shape[1:], OUT_LEN//t)
        
        print(model.summary())

        # Compile and train the model
        checkpoint = tf.keras.callbacks.ModelCheckpoint(
            os.path.join(WEIGHT_DIR, full_name + '.hdf5'),
            monitor='val_loss', verbose=1, save_best_only=True,
            save_weights_only=True, mode='min'
        )

        model.compile(
            loss=Balanced_CE,
            optimizer=tf.keras.optimizers.Adam(learning_rate=1e-4),
            metrics=['accuracy', Balanced_CE]
        )

        hist = model.fit(trainX, trainY_binary, verbose=2, validation_data=(valX, valY_binary),
                         epochs=EPOCHS, batch_size=BATCHES, callbacks=[checkpoint])

        # Save and plot results as in your original code
