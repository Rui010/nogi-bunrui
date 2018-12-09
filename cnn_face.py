import numpy as np
from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers.convolutional import Conv2D
from keras.layers.pooling import MaxPool2D
from keras.layers import Dense, Activation, Flatten
from keras.optimizers import SGD, Adam
import matplotlib.pyplot as plt

# 乱数シード
rng = np.random.RandomState(1234)
random_state = 42

# 学習データ
X = np.load('./data/x_train.npy')
t = np.load('./data/t_train.npy')
x_train, x_test, t_train, t_test = train_test_split(X, t, test_size=0.2, random_state=random_state)
x_train, x_valid, t_train, t_valid = train_test_split(x_train, t_train, test_size=0.1, random_state=random_state)

n_hidden = 200
n_out = len(t[0])
# print(np.shape(X))S

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

hist = model.fit(x_train, t_train, epochs=50,batch_size=10,validation_data=(x_valid, t_valid))

val_acc = hist.history['val_acc']
val_loss = hist.history['val_loss']

fig = plt.figure()
plt.plot(range(len(val_loss)), val_loss, label='loss')
plt.xlabel('epochs')
plt.show()

loss_and_metrics = model.evaluate(x_test, t_test)
print(loss_and_metrics)