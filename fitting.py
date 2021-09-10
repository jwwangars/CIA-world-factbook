# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# Step 3: fit a RNN model
# structure: embedding - RNN - dense - dense - (output)
# find residuals

import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation
from tensorflow.keras.layers import Embedding
from tensorflow.keras.layers import SimpleRNN
import numpy as np

model = Sequential()
model.add(Embedding(output_dim = 8,
                    input_dim = 4000,
                    input_length = 500))
model.add(SimpleRNN(units = 16))
model.add(Dense(units = 128,activation = 'relu'))
model.add(Dropout(0.05))
model.add(Dense(units=1,activation='linear'))


model.compile(loss='mse',optimizer='adam',metrics=['accuracy'])
history = model.fit(text_ts_input[error_count==0],pd.DataFrame(response[error_count==0]),batch_size = 16,
                    epochs = 5, verbose = 2, validation_split=0.2)
pred_error = pd.DataFrame(response[error_count==0]) - model.predict(text_ts_input[error_count==0])
pred_error.index = np.array(entity)[error_count==0]