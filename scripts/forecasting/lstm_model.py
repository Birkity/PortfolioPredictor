import logging
import numpy as np
import tensorflow as tf
from sklearn.preprocessing import MinMaxScaler

def preprocess_data(data, window_size):
   
    scaler = MinMaxScaler(feature_range=(0, 1))
    data_scaled = scaler.fit_transform(data.values.reshape(-1, 1))

    x, y = [], []
    for i in range(window_size, len(data_scaled)):
        x.append(data_scaled[i - window_size:i, 0])
        y.append(data_scaled[i, 0])

    logging.info(f"Data preprocessed for LSTM. Total sequences: {len(x)}.")
    return np.array(x), np.array(y), scaler

def build_lstm(input_shape):
    
    model = tf.keras.Sequential([
        tf.keras.layers.LSTM(50, return_sequences=True, input_shape=input_shape),
        tf.keras.layers.LSTM(50),
        tf.keras.layers.Dense(1)
    ])

    model.compile(optimizer='adam', loss='mean_squared_error')
    logging.info("LSTM model built and compiled.")
    return model

def train_lstm(model, x_train, y_train, epochs=50, batch_size=32):
   
    logging.info(f"Training LSTM model. Epochs: {epochs}, Batch size: {batch_size}.")
    try:
        model.fit(x_train, y_train, epochs=epochs, batch_size=batch_size, verbose=1)
        logging.info("LSTM model trained successfully.")
        return model
    except Exception as e:
        logging.error(f"Error during LSTM training: {str(e)}")
        raise
