# Deep Computer Vision
# Tenserflow implementaion with Keras
# pip install caer
# we will use kaggle GPU for this program (use kaggel notebook)
# Dataset: simson chararacter dataset

import os
import caer
import numpy as np
import cv2 as cv
import gc

IMG_SIZE = (80, 80)
channels = 1   # Grayscale
char_path = r'simpsons_dataset'   # Path where the dataset is

# Show the top 10 highest number of image in all the simpsons character
char_dict = {}
for char in os.listdir(char_path):
	char_dict[char] = len(os.listdir(os.path.join(char_path, char)))

# Sort in descending order
char_dict = caer.sort_dict(char_dict, descending=True)
# char_dict

# Grab the name of the first 10 character and store it in a list 
characters = []
for i in char_dict:
	characters.append(i[0])
	count += 1
	if count >= 10:
		break
# characters

# Create the training data
train = caer.preprocess_from_dir(char_path, characters, channels=channels, IMG_SIZE=IMG_SIZE, isShuffle=True, verbose=0)

len(train)

import matplotlib.pyplot as plt
plt.figure(figsize=(30,30))
plt.imshow(train[0][0], cmap='gray')
plt.show()

featureSet, labels = caer.sep_train(train, IMG_SIZE=IMG_SIZE)

from tensorflow.keras.utils import to_categorical
# Normalize the featureSet ==> (0,1)
featureSet = caer.normalize(featureSet)
labels = to_categorical(labels, len(characters))

x_train, x_val, y_train, y_val = caer.train_val_split(featureSet, labels, val_ratio=.2)

del train
del featureSet
del labels
gc.collect()

# Image data generator
datagen = canaro.generators.imageDataGenerator()
train_gen = datagen.flow(x_train, y_train, batch_size=BATCH_SIZE)

# Creating the model
model = canaro.models.createSimpsonsModel(IMG_SIZE=IMG_SIZE, channels=channels, output_dims=len(characters),
	                                      loss= 'binary_crossentropy', decay=1e-6, learning_rate=0.001,
	                                      momentum=0.9, nesterov=True)
model.summery()

from tensorflow.keras.callbacks import LearningRateScheduler
callbacks_list = [LearningRateScheduler(canaro.lr_schedule)]

# Train the model
training = model.fit(train_gen, 
	                 steps_per_epoch=len(x_train)//BATCH_SIZE,
                     epoch=EPOCHES,
                     validation_date=(x_val, y_val),
                     validation_steps=len(y_val)//BATCH_SIZE,
                     callbacks=callbacks_list)

# Test how good the model is with openCV
test_path = r'bart_simpsons.jpg'   # put a image path to classify

img = cv.imread(test_path)
# plt.imshow(img, cmap='gray')
# plt.show()

def prepare(img):
	img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
	img = cv.resize(img, IMG_SIZE)
	img = cear.reshape(img, IMG_SIZE, 1)
	return img

predictins = model.predict(prepare(img))

# predictions

print(characters[np.argmax(predictions[0])])



