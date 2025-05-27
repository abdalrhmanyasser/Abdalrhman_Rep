import os
import glob as gb
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image
import cv2
#These packages help with building, training, and analyzing the CNN.
import tensorflow as tf
import keras
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Dense, Dropout, Flatten, GlobalAveragePooling2D
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
#@title
ImageSize = 224 #@param {type:"integer"}
#Declaring constants.
PATH=R'C:\Users\abdal\Downloads\Celebrity_Faces_Dataset' #Change the path so that it points to the celebrity dataset on your Drive.

#Preliminary data visualization. It gives us a general idea of the distribution of the files between the different classes.
i = 0
for folder in os.listdir(PATH):
    files = gb.glob(pathname= str(f'{PATH}/{folder}/*.jpg'))
    print(f'There are {len(files)} images in {folder} folder')
    i+=1
print(f'There are a total of {i} folders!')
#Define a data dictionnary mapping each celebrity name
# to "its class", a numerical value representing the celebrity
# Numeric values are easier to handle by the DL algorithms we shall build
CelebCodes = {'Sandra_Bullock':0,
        'Angelina_Jolie':1,
        'Natalie_Portman':2,
        'Megan_Fox':3,
        'Tom_Cruise':4,
        'Kate_Winslet':5,
        'Leonardo_DiCaprio':6,
        'Jennifer_Lawrence':7,
        'Brad_Pitt':8,
        'Hugh_Jackman':9,
        'Will_Smith':10,
        'Nicole_Kidman':11,
        'Johnny_Depp':12,
        'Robert_Downey_Jr':13,
        'Tom_Hanks':14,
        'Scarlett_Johansson':15,
        'Denzel_Washington':16}
CelebKeys = list(CelebCodes.keys())
#The X is a list of pictures in the form numpy arrays (celebrity images).
X = []
#The y is a list of celebrity classes of the corresponding images.
y = []
for folder in os.listdir(PATH):
    files = gb.glob(pathname= str(f'{PATH}/{folder}/*.jpg'))
    for file in files:
        image = cv2.imread(file)
        image_array = cv2.resize(image, (ImageSize,ImageSize)) #Each of the images is resized to a uniform 224 x 224 size.
        X.append(list(image_array))
        y.append(CelebCodes[folder])
## Data Visualization

index = 120 #@param {type:"integer"} 50, 120
if index < len(X):
  plt.imshow(X[index])
  title = str(f'Class: {y[index]:02} -- Celebrity: {CelebKeys[y[index]]}')
  plt.title(title)
  plt.show()
else:
  print('Index out of range!')
#Each value in the y array is converted to a one-hot encoded array.
encoder = OneHotEncoder()
Y = encoder.fit_transform(np.array(y).reshape(-1,1)).toarray()
#The X and Y lists are converted to numpy arrays.
X = np.asarray(X)
Y = np.asarray(Y)
#The X and y arrays are split into train and test sub-datasets. Their ratio is 7:3 respectively.
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, random_state=1 , shuffle=True)

#Visualizing the train and test datasets.
print(X_train.shape)
print(X_test.shape)
print(y_test.shape)
print(y_train.shape)
#@title
BatchSize = 30 #@param {type:"integer"}
## Data Augmentation
#Creating a list of transformations that we will apply to each image. This process is known as image augmentation. It helps to make deep learning algorithms robust.
train_datagen = ImageDataGenerator(rescale = 1./255, #Converts each pixel value in the image array to a decimal value.
                                  )
test_datagen = ImageDataGenerator(rescale = 1./255) #Converts each pixel value in the image array to a decimal value.

#Applying the transformations to all the images.
train_iterator = train_datagen.flow(X_train, y_train, BatchSize)
test_iterator = test_datagen.flow(X_test, y_test, BatchSize)
print('Batches train=%d, test=%d, batch-size=%d' % (len(train_iterator), len(test_iterator), BatchSize)) #The ratio of the batch size of the train dataset to the test dataset is about 7:3.


### Building the Model
###Question Time!!
x_axis_size = 150 #@param {type:"integer"}
y_axis_size = 200 #@param {type:"integer"}
#@title
if x_axis_size != ImageSize and y_axis_size != ImageSize:
  print(f'Oh no! The input size needs to be the same as the image size: {ImageSize}x{ImageSize}')
else:
  print('Yay! You are correct!')
output_neuron = 17 #@param {type:"integer"}
#@title
if output_neuron != len(CelebKeys):
  print('Oh no! The number of output neurons need to be the same as the number of classes we are detecting: 17')
else:
  print('Yay! Your answer is correct!')
#Creating our CNN model!!!
model = Sequential()
model.add(Conv2D(32,kernel_size=(3,3),activation='relu',input_shape=(ImageSize,ImageSize,3)))
model.add(MaxPooling2D(2,2))
model.add(Conv2D(32,kernel_size=(4,4),activation='relu'))
model.add(MaxPooling2D(2,2))
model.add(Dropout(rate=0.5))
model.add(Flatten())
model.add(Dense(len(CelebKeys),activation='softmax'))
### Learning Rate
# The learning rate is a parameter used in training machine learning models, specifically in optimization algorithms like gradient descent. It determines the step size taken in adjusting the model's parameters during the learning process.

# Imagine you are climbing a mountain, and you want to reach the top by taking small steps. The learning rate is like the size of the steps you take. If the learning rate is too large, you might overshoot the optimal point and miss the peak. On the other hand, if the learning rate is too small, you might take forever to reach the top or get stuck in a suboptimal position.
LearningRate = 0.006 #@param {type:"slider", min:0.0000001, max:1, step:1e-8}
#Creating a Adam optimizer, with a learning rate of 1e-3. The learning rate is a hyperparameter that can be adjusted to improve the performance of the model.
opt = tf.keras.optimizers.Adam(LearningRate)
model.compile(optimizer=opt, loss='categorical_crossentropy',metrics=['accuracy'])
#Visualizing the model.
print('Model Details are : ')
print(model.summary())
## Epochs
# In DL, an epoch refers to a complete pass through the entire training dataset during the model training process. It helps in determining how many times the model will iteratively learn from the training data.

# Imagine you have a book that you want to read and understand thoroughly. Instead of reading it all at once, you decide to read it chapter by chapter. Each time you read through all the chapters of the book, you complete one epoch.
NumEpochs = 300 #@param {type:"slider", min:2, max:20, step:1}
#Train the model for 80 epochs. The number of epochs can be increased, which usually improves the performance of the model.
History = model.fit(X_train, y_train,  steps_per_epoch=len(train_iterator), epochs=NumEpochs)
#Testing the model on the testing dataset.
test_eval = model.evaluate(X_test, y_test, batch_size=BatchSize)
print('Test loss:', test_eval[0])
print('Test accuracy:', test_eval[1])
# Our contructed model does not receive a very high accuracy score because it has only been trained for a few epochs, and because it has a small brain. To improve the accuracy of a model, you may choose to increase it size (number of layers and structure), and change its hyperparameters to improve performance. For example, you may choose to modify the learning rate, or increase the number of epochs that you train the CNN for.

# In the next section, you will go against a bigger model that has been trained for 500 epochs and achieves an accuracy score that is very close to 100%.

#Let us load a pretrained model that has good accuracy
#Load the file where the model is stored
PATHModel='/content/drive/MyDrive/Colab Notebooks'
MFName = str(f'{PATHModel}/M17.h5')
#
#load the model so we can work with it
Model500 = keras.models.load_model(MFName)
#Testing the loaded model on the testing dataset.
test_eval = Model500.evaluate(X_test, y_test, batch_size=BatchSize)
#Predicting values on the test dataset.
pred_test = Model500.predict(X_test)
y_pred = encoder.inverse_transform(pred_test)
y_t = encoder.inverse_transform(y_test)
print('Test loss:', test_eval[0])
print('Test accuracy:', test_eval[1])
# Your model does not receive a very high accuracy score because it has only been trained for a few epochs. To improve the accuracy of a model, you may choose to change its hyperparameters to improve performance. For example, you may choose to modify the learning rate, or increase the number of epochs that you train the CNN for.

# In the next section, you will go against a model that has been trained for 500 epochs and achieves an accuracy score that is very close to 100%.
# **Now let's test you against a computer. You will be shown an image, choose the name of the celebrity, and then let's see what the model we just trained thinks. Run the next code block as many times as you wish.**
#@title
import random
random_integer=random.randint(0, len(os.listdir(PATH)))
random_celebrity=f'{PATH}/{os.listdir(PATH)[random_integer]}'
file = f'{random_celebrity}/{os.listdir(random_celebrity)[random.randint(0, len(os.listdir(random_celebrity)))]}'
img = Image.open(file)
img
#@title
YourChoice = 'Sandra_Bullock' #@param ['Will_Smith','Scarlett_Johansson','Nicole_Kidman','Denzel_Washington','Johnny_Depp','Robert_Downey_Jr','Hugh_Jackman','Jennifer_Lawrence','Brad_Pitt','Leonardo_DiCaprio','Megan_Fox','Kate_Winslet','Angelina_Jolie','Tom_Cruise','Tom_Hanks','Sandra_Bullock','Natalie_Portman', 'Scarlett Johanson']
#@title define useful functions
def get_celebrity(n):
  for k, v in CelebCodes.items():
    if v == n: return k

def predict(img, model):
  img = img.resize((ImageSize, ImageSize), Image.LANCZOS)
  np_img = np.asarray(img)
  return get_celebrity(np.argmax(model.predict(np.expand_dims(np_img, axis=0))))
#predict using both model
GoodModelValue = predict(img, Model500)
BadModelValue = predict(img, model)
#@title
random_celebrity = random_celebrity.split('/')[-1]
print(f'The good pre-trained model predicted celebrity: {GoodModelValue}')
if GoodModelValue == random_celebrity:
    if YourChoice != random_celebrity:
      print('Oops! The model predicted correctly, but unfortunately, you did not')
    elif YourChoice== random_celebrity:
      print('Yay! Both you and the model predicted the celebrity correctly')
else:
    if YourChoice != random_celebrity:
      print('Oops! Both you and the model predicted incorrectly')
    elif YourChoice == random_celebrity:
      print('Yay! You predicted correctly, but unfortunately, the model did not')

print(f'The model that we just trained predicted celebrity is: {BadModelValue}')
#@title
# %%capture
#Saving the model using the JSON file. Saving the weights of the model using the H5 file. This makes it easier to access the file again from where we left it.
model_json = model.to_json()
with open("model_CNN_YP.json", "w") as json_file:
    json_file.write(model_json)
model.save_weights("model_CNN_celebrities.h5")
print("Saved model to disk")
#@title
# %%capture
#Loading the model again
json_file = open("model_CNN_YP.json", 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = keras.models.model_from_json(loaded_model_json)
loaded_model.load_weights("model_CNN_celebrities.h5")
print("Loaded model from disk")
#@title
#Placing all the values from the model prediction onto a dataframe.
df = pd.DataFrame(columns=['Predicted Labels', 'Actual Labels'])
df['Predicted Labels'] = y_pred.flatten()
df['Actual Labels'] = y_t.flatten()
#@title
#Creating a confusion matrix. This helps visualize what the model predicted versus what the actual value of the images were.
cm  = confusion_matrix(y_t, y_pred ,normalize='true')
plt.figure(figsize = (12, 10))

CNN=[cm[0,0],cm[1,1],cm[2,2],cm[3,3],cm[4,4]]
CNN= pd.DataFrame(CNN)

x_label=np.array(CelebKeys)
y_label=np.array(CelebKeys)

cmYP = pd.DataFrame(cm, index = x_label, columns = y_label,)

sns.heatmap(cmYP, linecolor='white', cmap='Blues', linewidth=2, annot=True, )
plt.title('Confusion Matrix', size=20)
plt.xlabel('Predicted Labels', size=14)
plt.ylabel('Actual Labels', size=14)
plt.show()