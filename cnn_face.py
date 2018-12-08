import numpy as np
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers.convolutional import Conv2D
from keras.layers.pooling import MaxPool2D
from keras.layers import Dense, Activation, Flatten
from keras.optimizers import SGD, Adam

# 乱数シード
# rng = np.random.RandomState(1234)
random_state = 42

# 学習データ
X = np.load('./data/x_train.npy')
t = np.load('./data/t_train.npy')
# x_train, x_valid, t_train, t_valid = train_test_split(X, t, test_size=0.5, random_state=random_state)

n_in = len(X[0])
n_hidden = 200
n_out = len(t[0])
print(np.shape(X))

model = Sequential([
    Conv2D(32,3,input_shape=(64,64,3)),
    Activation('relu'),
    Flatten(),
    Dense(n_hidden),
    Activation('relu'),
    Dense(n_out),
    Activation('softmax')
])

model.compile(
    loss='categorical_crossentropy', 
    optimizer=SGD(lr=0.1),
    metrics=['accuracy']
)

model.fit(X, t, epochs=10, batch_size=1)

classes = model.predict_classes(X, batch_size=1)
prob = model.predict_proba(X, batch_size=1)

print('classified:')
print(t == classes)
print('output probability:')
print(prob)