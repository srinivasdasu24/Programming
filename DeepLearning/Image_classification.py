#!/usr/bin/env python
# coding: utf-8

# In[1]:


# keras fashion MNIST dataset. This consist of 60000 28X28 pixel images and 10000 test images
# keras fashion MNIST dataset. This consist of 60000 28X28 pixel images and 10000 test images
import keras
import matplotlib.pyplot as plt
import numpy as np

get_ipython().run_line_magic('matplotlib', 'inline')

# In[2]:


keras.backend.backend()

# In[3]:


fm = keras.datasets.fashion_mnist
(x_train, y_train), (x_test, y_test) = fm.load_data()

# In[4]:


x_train.shape

# In[5]:


x_test.shape

# In[6]:


x_train[0]

# In[7]:


plt.matshow(x_train[0])

# In[8]:


print(y_train[0])

# In[9]:


x_train = x_train / 255
x_test = x_test / 255

# In[46]:


from keras.models import Sequential
from keras.layers import Dense, Flatten

model = Sequential()
input = model.add(Flatten(input_shape=[28, 28]))

# In[61]:


model.add(Dense(120, activation='relu'))
model.add(Dense(120, activation='relu'))

model.add(Dense(10, activation='softmax'))

# In[62]:


model.summary()

# In[63]:


model.compile(loss='sparse_categorical_crossentropy', optimizer='adam',
              metrics=["accuracy"])

# In[64]:


model.fit(x_train, y_train, epochs=3)

# In[65]:


model.evaluate(x_test, y_test)

# In[66]:


plt.matshow(x_test[0])

# In[67]:


yp = model.predict(x_test)

# In[54]:


np.argmax(yp[0])

# In[19]:


class_labels = {

    0: "T-shirt/top",
    1: "Trouser",
    2: "Pullover",
    3: "Dress",
    4: "Coat",
    5: "Sandal",
    6: "Shirt",
    7: "Sneaker",
    8: "Bag",
    9: "Ankle boot"}

# In[20]:


print(class_labels[np.argmax(yp[0])])

# In[ ]:
