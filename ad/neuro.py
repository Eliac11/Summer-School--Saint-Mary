from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Dense, Flatten, Dropout, Activation


model = Sequential([
        Dense(200, input_dim=64),
        Activation('relu'),
        Dropout(0.2),
        Dense(4)
    ])
model.compile('adadelta', 'mse')
