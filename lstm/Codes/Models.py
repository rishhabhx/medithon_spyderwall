#%% Import modules
import tensorflow as tf
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, SimpleRNN, Dense, LSTM, Flatten, Conv1D, GRU
from tensorflow.keras.layers import Bidirectional
from ncps import wirings
from ncps.keras import LTC
from tensorflow import keras

#%% Models
def RNNs(input_shape, output_shape):
    inputs = Input(shape = input_shape, name = 'X')
    X = SimpleRNN(units=96, return_sequences=True)(inputs)
    X = SimpleRNN(units=48, activation='relu', return_sequences=True)(X)
    X = SimpleRNN(units=24, activation='relu', return_sequences=True)(X)
    X = Flatten()(X)
    outputs = Dense(units= output_shape, activation='sigmoid')(X)
    model = Model(inputs = inputs, outputs = outputs)
    return model

def GRUs(input_shape, output_shape):
    inputs = Input(shape = input_shape, name = 'X')
    X = GRU(units=48, activation='tanh', return_sequences=True)(inputs)
    X = GRU(units=24, activation='tanh', return_sequences=True)(X)
    X = GRU(units=12, activation='tanh', return_sequences=True)(X)
    X = Flatten()(X)
    outputs = Dense(units = output_shape, activation='sigmoid')(X)
    model = Model(inputs = inputs, outputs = outputs)
    return model

def LSTMs(input_shape, output_shape):
    inputs = Input(shape = input_shape, name = 'X')
    X = LSTM(units=48, activation='tanh', return_sequences=True)(inputs)
    X = LSTM(units=24, activation='tanh', return_sequences=True)(X)
    X = LSTM(units=12, activation='tanh', return_sequences=True)(X)
    X = Flatten()(X)
    outputs = Dense(units = output_shape, activation='sigmoid')(X)
    model = Model(inputs = inputs, outputs = outputs)
    return model

def BiLSTMs(input_shape, output_shape):
    inputs = Input(shape = input_shape, name = 'X')
    X = Bidirectional(LSTM(units=24, activation='tanh', return_sequences=True))(inputs)
    X = Bidirectional(LSTM(units=16, activation='tanh', return_sequences=True))(X)
    X = Bidirectional(LSTM(units=12, activation='tanh', return_sequences=True))(X)
    X = Flatten()(X)
    outputs = Dense(units = output_shape, activation='sigmoid')(X)
    model = Model(inputs=inputs, outputs=outputs)
    return model

def CNN_LSTMs(input_shape, output_shape):
    inputs = Input(shape =input_shape, name = 'X')
    X = Conv1D(filters=64, kernel_size=1,strides=1, activation='relu', padding='same')(inputs)
    X2 = Conv1D(filters=32, kernel_size=3,strides=1, activation='relu', padding='same')(X)
    X3 = Conv1D(filters=32, kernel_size=5,strides=1, activation='relu', padding='same')(X)
    X4 = tf.keras.layers.concatenate([X2,X3])
    X5 = Conv1D(filters=1, kernel_size=1,strides=1, activation='relu', padding='same')(X4)
    f_X = LSTM(units=output_shape*2, activation='tanh', return_sequences=True)(inputs)
    f_X2= Dense(units = 1)(f_X)
    outputs_ = tf.math.add(f_X2,X5)
    outputs  = tf.math.sigmoid(outputs_)
    model = Model(inputs=inputs, outputs=outputs)
    return model

def Transformers(input_shape, output_shape):
    inputs = Input(shape=input_shape, name='X')
    qx = tf.keras.layers.Conv1D(24, 8, 1, padding='same', activation='relu')(inputs)
    ## self-attention
    attention = tf.keras.layers.MultiHeadAttention(num_heads=24, key_dim=4)(qx, qx)
    x = tf.keras.layers.Add()([qx, attention])  # residual connection
    layernorm1 = tf.keras.layers.LayerNormalization(epsilon=1e-6)(x)
    ## Feed Forward
    x = tf.keras.layers.Conv1D(24, 8, 1, padding='same')(layernorm1)
    x2 = tf.keras.layers.Conv1D(24, 8, 1, padding='same')(x)
    x3 = tf.keras.layers.Flatten()(x2)
    outputs = Dense(units=output_shape, activation='sigmoid')(x3)
    model = Model(inputs=inputs, outputs=outputs)
    return model

# %% LNN model testing
def lnn(ip_shape, output_shape):
    # Define the architecture for the Liquid Time-Constant Network (LTC)
    # Here, 'AutoNCP' creates a wiring configuration with 8 input units and 1 output unit
    ncp_arch = wirings.AutoNCP(8, 1)

    # Create a sequential model using Keras
    ncp_model = keras.models.Sequential(
        [
            # Input layer expects sequences of length None (variable length) with 2 features
            keras.layers.InputLayer(input_shape=ip_shape),
            
            # Add the LTC layer with the previously defined architecture
            # The layer is set to return sequences, making it suitable for time series tasks
            LTC(ncp_arch, return_sequences=True),
            # Flatten the output
            keras.layers.Flatten(),
            # Output layer with the specified output shape
            keras.layers.Dense(units=output_shape, activation='sigmoid')
        ]
    )

    # Compile the model with the Adam optimizer and mean squared error loss function
    ncp_model.compile(
        optimizer=keras.optimizers.Adam(0.01),  # Learning rate set to 0.01
        loss='mean_squared_error'  # Common loss function for regression tasks
    )

    # Display the model's summary, which provides an overview of the architecture and parameters
    ncp_model.summary()
    return ncp_model
# %%
