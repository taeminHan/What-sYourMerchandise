from tensorflow import keras
from tensorflow.keras import utils
from tensorflow.keras import layers
from tensorflow.keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPooling2D
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import os

data_path = 'C:/Users/taemin/PycharmProjects/What-sYourMerchandise/DataSet/Train'
categories = os.listdir(data_path)
labels = [i for i in range(len(categories))]

label_dic = dict(zip(categories, labels))

print(label_dic)