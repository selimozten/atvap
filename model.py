import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense

class LSTMModel:
    def __init__(self, look_back):
        self.look_back = look_back
        self.model = self._build_model()

    def _build_model(self):
        model = Sequential([
            LSTM(50, activation='relu', input_shape=(self.look_back, 1)),
            Dense(1)
        ])
        model.compile(optimizer='adam', loss='mse')
        return model

    def train(self, X, y, epochs=100, batch_size=32):
        self.model.fit(X, y, epochs=epochs, batch_size=batch_size, verbose=1)

    def predict(self, X):
        return self.model.predict(X)