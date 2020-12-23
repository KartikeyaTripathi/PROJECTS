# -*- coding: utf-8 -*-
"""MLProject-1



Original file is located at
    https://colab.research.google.com/github/KartikeyaTripathi/Google-Kickstart/blob/master/MLProject_1.ipynb
"""

import keras

from keras.datasets import mnist

data = mnist.load_data()
(train_images, train_labels), (test_images, test_labels) = data

len(train_images)

len(test_images)

len(test_labels)

train_images = train_images.reshape((60000, 28, 28, 1))

test_images = test_images.reshape((10000, 28, 28, 1))

train_images = train_images.astype('float')/255 #normalization/scaling

test_images = test_images.astype('float')/255

from keras.preprocessing import image
import matplotlib.pyplot as plt

plt.imshow(image.array_to_img(train_images[8]), cmap = "gray")

train_labels[8]

from keras.utils import to_categorical
train_labels_original = train_labels
train_labels = to_categorical(train_labels)

train_labels[20]

test_labels_original = test_labels
test_labels = to_categorical(test_labels)

test_labels_original[7]

test_labels[7]

from keras import layers, models

model = models.Sequential()

model.add(layers.Conv2D(32, (3,3),activation='relu', input_shape = (28,28,1)))



model.summary()

model.add(layers.MaxPooling2D((2,2)))

model.add(layers.Conv2D(64, (3,3), activation= 'relu'))

model.summary()

model.add(layers.MaxPooling2D((2,2)))

model.add(layers.Conv2D(64, (3,3), activation='relu'))

model.summary()

model.add(layers.Flatten())

model.summary()

model.add(layers.Dense(64, activation = 'relu'))

model.add(layers.Dense(10,activation= 'softmax'))

model.summary()

model.compile(loss='categorical_crossentropy',optimizer='rmsprop', metrics=['accuracy'])

model.fit(train_images, train_labels, epochs = 100, batch_size=64)

test_loss, test_accuracy = model.evaluate(test_images, test_labels)

test_accuracy

predictions = model.predict_classes(test_images)

plt.imshow(image.array_to_img(test_images[999]), cmap="gray")

predictions[999]

plt.imshow(image.array_to_img(test_images[8888]))

predictions[8888]

plt.imshow(image.array_to_img(test_images[3245]))

predictions[3245]
