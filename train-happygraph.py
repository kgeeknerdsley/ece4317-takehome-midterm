import tensorflow as tf
import numpy as np
from tensorflow import keras
import csv

datapath_x = "/home/kevin/Desktop/hg_x.txt"
datapath_y = "/home/kevin/Desktop/hg_y.txt"

mnist = tf.keras.datasets.mnist #common dataset for optical character recognition

(x_train, y_train), (x_test, y_test) = mnist.load_data() #load in data to numpy arrays
x_train, x_test = x_train / 255.0, x_test / 255.0 #normalize pixel colors to grayscale

model = tf.keras.models.Sequential([ #extremely basic CNN
  tf.keras.layers.Flatten(input_shape=(28, 28)),
  tf.keras.layers.Dense(128, activation='relu'),
  tf.keras.layers.Dropout(0.2),
  tf.keras.layers.Dense(10)
])

loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True) #categorical identification loss

model.compile(optimizer='adam', #get the model in a workable state
              loss=loss_fn,
              metrics=['accuracy'])

#----Trials----
#Model is trained on dataset amount increasing by 10 every step
#Record the testing accuracy (no averages needed, all return same value)
#Write out to text file for graphing

averagedAcc = 0

for i in range(1,100):
    averagedAcc = 0
    x_train_modified = np.delete(x_train, np.arange(i*10,60000),0) #delete most of the 60000 images, save only step * 10
    y_train_modified = np.delete(y_train, np.arange(i*10,60000),0) #do it to labels too

    print("Dataset size = " + str(x_train_modified.shape) + "\n")

    model.fit(x_train_modified, y_train_modified, epochs=5) #train the model in 5 epochs

    value = model.evaluate(x_test,  y_test, verbose=2) #test the model's accuracy
    print(str(value[1]) + "\n")

    xfile = open(datapath_x, 'a+') #write out x values
    xfile.write(str(i*10) + "\n")
    

    yfile = open(datapath_y, 'a+') #write out y values
    yfile.write(str(value[1]) + "\n")

    keras.backend.clear_session() #clear the training weights so we start from scratch every pass

xfile.close()
yfile.close()

