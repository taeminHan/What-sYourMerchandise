from PIL import Image
import os, glob, numpy as np
from sklearn.model_selection import train_test_split
import os, glob, numpy as np
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Dense, Flatten, Dropout
from keras.callbacks import EarlyStopping, ModelCheckpoint
import matplotlib.pyplot as plt
import tensorflow as tf

# TODO: 2021. 1. 2. 일단은 클론코딩으로 시작. 데이터 수가 너무 부족하다 더 수집해야 한다.

caltech_dir = 'C:/Users/taemin/PycharmProjects/What-sYourMerchandise/DataSet/Train'
categories = ["Cocacola", "sevenstar", "sprite"]
nb_classes = len(categories)

image_w = 64
image_h = 64

pixels = image_h * image_w * 3

X = []
y = []

for idx, cat in enumerate(categories):

    # one-hot 돌리기.
    label = [0 for i in range(nb_classes)]
    label[idx] = 1

    image_dir = caltech_dir + "/" + cat
    files = glob.glob(image_dir + "/*.jpg")
    print(cat, " 파일 길이 : ", len(files))
    for i, f in enumerate(files):
        img = Image.open(f)
        img = img.convert("RGB")
        img = img.resize((image_w, image_h))
        data = np.asarray(img)

        X.append(data)
        y.append(label)

        if i % 700 == 0:
            print(cat, " : ", f)

X = np.array(X)
y = np.array(y)
# 1 0 0 0 이면 airplanes
# 0 1 0 0 이면 buddha 이런식


X_train, X_test, y_train, y_test = train_test_split(X, y)
xy = (X_train, X_test, y_train, y_test)
np.save("C:/Users/taemin/PycharmProjects/What-sYourMerchandise/multi_image_data.npy", xy)

print("ok", len(y))

config = tf.compat.v1.ConfigProto()
"""
    config  :   
                tensorflow 2.x 버전 업데이트 이후 
                tf.ConfigProto() -> tf.compat.v1.ConfigProto()
"""
config.gpu_options.allow_growth = True
session = tf.compat.v1.Session(config=config)
"""
    session  :   
                tensorflow 2.x 버전 업데이트 이후 
                tf.session() -> tf.compat.v1.session()
"""

X_train, X_test, y_train, y_test = np.load('C:/Users/taemin/PycharmProjects/What-sYourMerchandise/multi_image_data.npy')
print(X_train.shape)
print(X_train.shape[0])
