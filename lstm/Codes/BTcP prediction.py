# %% Import modules
import os, sys, pickle
import tensorflow as tf


# %% Import custom modules
ROOT = r"/home/jaz/coding/BTcP-prediction-main/"
# sys.path.append(os.path.join(ROOT, 'Codes'))
from Utils import *
from Models import LSTMs
from Losses import Balanced_CE
ROOT


# %% Set hyper parameters
EX        = 'BTcP prediction'
EPOCHS  = 300
BATCHES = 100
IN_LENS = [120, 72, 24]
OUT_LEN = 24
TAUS    = [1,2,3,4,6,8,12]


# %% Directories
DATA_DIR   = os.path.join(ROOT, 'Example datasets')
SAVE_DIR   = os.path.join(ROOT, 'Results')
WEIGHT_DIR = os.path.join(ROOT, 'Weights')
makedirs(SAVE_DIR)
makedirs(WEIGHT_DIR)
DATA_DIR


# %% Loop for train and test (double loops, loop 1: for input lengths, loop 2: for time bin size)
for IN_LEN in IN_LENS:
    # Load dataset according to input lengths
    with open(os.path.join(DATA_DIR, 'data for '+str(IN_LEN)+' hours.pickle'), 'rb') as f:
        data = pickle.load(f)

    # for plots according to resolutions
    tprs, fprs, aurocs, auprcs, pres, recs = [], [], [], [], [], []

    for t in TAUS:
        # split data into train/val/test (6/2/2)
        train, val, test = np.split(data['data'], [int(.6 * len(data['data'])), int(.8 * len(data['data']))])

        # Time binning
        train = time_binning(train, t)
        test = time_binning(test, t)
        val = time_binning(val, t)

        trainX, trainY = split_XY(train, IN_LEN//t)
        testX_, testY = split_XY(test, IN_LEN//t)
        valX, valY = split_XY(val, IN_LEN//t)

        # Transformation (72 hours records ->  shape of (24,3))
        trainX, valX, testX = transformation(trainX, valX, testX_, t)

        # Make Y as Binary score
        trainY_binary, valY_binary, testY_binary = make_binary_score_for_all(trainY, valY, testY)

        #Squeeze Y shape
        testY_binary = np.squeeze(testY_binary)
        trainY_binary = np.squeeze(trainY_binary)
        valY_binary = np.squeeze(valY_binary)

        # Models
        full_name = '_'.join([str(IN_LEN), str(OUT_LEN), 'LSTM', str(t)])

        # Set model
        model = LSTMs(trainX.shape[1:], OUT_LEN//t)
        print(model.summary())

        # Train
        # checkpoint = tf.keras.callbacks.ModelCheckpoint(os.path.join(WEIGHT_DIR, full_name + '.hdf5'),
        #                                                 monitor='val_Balce', verbose=1, save_best_only=True,
        #                                                 save_weights_only=True, mode='min', period=1)
        # model.compile(loss=Balanced_CE, optimizer=tfa.optimizers.SWA(Adam(lr=1e-4), start_averaging=5, average_period=1), metrics=['acc', Balanced_CE])
        # hist = model.fit(trainX, trainY_binary, verbose=2, validation_data=(valX, valY_binary), epochs=EPOCHS, batch_size=BATCHES, callbacks=[checkpoint])
        # plot(hist.history, os.path.join(SAVE_DIR,'{} Learning curves.jpg'.format(full_name)))

        # Test
        model.load_weights(os.path.join(WEIGHT_DIR, full_name+'.hdf5'))
        pred_prob = model.predict(testX)
        pred_prob = np.squeeze(pred_prob)
        pred  = np.squeeze(np.round(pred_prob))


        # AUC PR/ROC
        fpr, tpr, thresh = metrics.roc_curve(testY_binary.reshape(-1), pred_prob.reshape(-1))
        auc = metrics.roc_auc_score(testY_binary.reshape(-1), pred_prob.reshape(-1))
        tprs.append(tpr)
        fprs.append(fpr)
        aurocs.append(auc)

        lr_precision, lr_recall, _ = metrics.precision_recall_curve(testY_binary.reshape(-1), pred_prob.reshape(-1))
        lr_auc = metrics.auc(lr_recall, lr_precision)
        pres.append(lr_precision)
        recs.append(lr_recall)
        auprcs.append(lr_auc)


    plt.clf()
    plt.figure(figsize=(4.5, 4.5))
    for fpr, tpr, auc, t in zip(fprs, tprs, aurocs, TAUS):
        plt.plot(fpr, tpr, lw=2, label="τ = %s : %0.4f" % (str(t), auc))
    plt.xlim([0., 1.])
    plt.ylim([0., 1.])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('ROC curve')
    plt.legend(loc="lower right")
    plt.savefig(os.path.join(SAVE_DIR, str(IN_LEN)+'_for T_AUC-ROC.svg'))
    plt.clf()


    plt.figure(figsize=(4.5, 4.5))
    for lr_recall, lr_precision, lr_auc, t in zip(recs, pres, auprcs, TAUS):
        plt.plot(lr_recall, lr_precision, lw=2, label="τ = %s : %0.4f" % (str(t), lr_auc))
    plt.xlim([0., 1.])
    plt.ylim([0., 1.])
    plt.xlabel('Recall')
    plt.ylabel('Precision')
    plt.title('PR curve')
    plt.legend(loc="lower right")
    plt.rc('font', size=10)
    plt.savefig(os.path.join(SAVE_DIR, str(IN_LEN)+'_for T_AUC-PR.svg'))
    plt.clf()
   
 


# %% Import custom LNN model

import os
import pickle
import numpy as np
import tensorflow as tf
from Models import lnn

# Loop for training and testing
# Loop for training and testing
for IN_LEN in IN_LENS:
    # Load the data
    with open(os.path.join(DATA_DIR, 'data for ' + str(IN_LEN) + ' hours.pickle'), 'rb') as f:
        data = pickle.load(f)

    for t in TAUS:
        train, val, test = np.split(data['data'], [int(.6 * len(data['data'])), int(.8 * len(data['data']))])

        # Time binning
        train = time_binning(train, t)
        test = time_binning(test, t)
        val = time_binning(val, t)

        trainX, trainY = split_XY(train, IN_LEN//t)
        testX_, testY = split_XY(test, IN_LEN//t)
        valX, valY = split_XY(val, IN_LEN//t)

        # Transformation (72 hours records ->  shape of (24,3))
        trainX, valX, testX = transformation(trainX, valX, testX_, t)

        # Make Y as Binary score
        trainY_binary, valY_binary, testY_binary = make_binary_score_for_all(trainY, valY, testY)

        #Squeeze Y shape
        testY_binary = np.squeeze(testY_binary)
        trainY_binary = np.squeeze(trainY_binary)
        valY_binary = np.squeeze(valY_binary)
        
        # model
        full_name = '_'.join([str(IN_LEN), str(OUT_LEN), 'LNN', str(t)])
        model = lnn(trainX.shape[1:], OUT_LEN // t)

        print(model.summary())

        # Compile and train the model
        checkpoint = tf.keras.callbacks.ModelCheckpoint(
            os.path.join(WEIGHT_DIR, full_name + '.weights.h5'),
            monitor='val_loss', verbose=1, save_best_only=True,
            save_weights_only=True, mode='min'
        )

        # Compile the model using binary_crossentropy
        model.compile(
            loss='binary_crossentropy',  # Updated to binary cross-entropy
            optimizer=tf.keras.optimizers.Adam(learning_rate=1e-4),
            metrics=['accuracy']  # Optionally, add other metrics like 'AUC', 'Precision', 'Recall'
        )

        # Optional: Class weighting to handle imbalanced data
        class_weight = {0: 0.5, 1: 1.5}  # Adjust based on your data's imbalance
        # Flatten the labels to 1D
        trainY_binary = trainY_binary.reshape(-1)
        valY_binary = valY_binary.reshape(-1)

        hist = model.fit(
            trainX, trainY_binary, 
            verbose=2, validation_data=(valX, valY_binary),
            epochs=EPOCHS, batch_size=BATCHES, callbacks=[checkpoint],
            class_weight=class_weight  # If still causing issues, consider removing this line
        )


        # Save and plot results as in your original code


# %%
