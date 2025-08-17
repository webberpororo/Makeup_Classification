# import keras
# import tensorflow as tf
# import numpy as np
# from tensorflow.keras.models import Sequential, Model
# from tensorflow.keras.layers import Dense, Conv2D, MaxPooling2D, Flatten, Dropout, BatchNormalization, ReLU, \
#     GlobalAveragePooling2D, Activation, Add, Input
# from tensorflow.keras.optimizers import Adam
# from tensorflow.keras.regularizers import l1, l2
# from tensorflow.keras.datasets import mnist, fashion_mnist, cifar10
# from sklearn.model_selection import train_test_split
# from tensorflow.keras.utils import to_categorical
# from tensorflow.keras.preprocessing.image import ImageDataGenerator
# from tensorflow.keras.models import load_model
# from tensorflow import lite
# import tensorflow_hub as hub
# from tensorflow.keras.applications import DenseNet121
# import matplotlib.pyplot as plt
#
# # # (x_train, y_train), (x_test, y_test) = mnist.load_data()
# # (x_train, y_train), (x_test, y_test) = fashion_mnist.load_data()
# # # (x_train, y_train), (x_test, y_test) = cifar10.load_data()
# # # print(y_test)
# # x_all = np.concatenate((x_train, x_test), axis=0)
# # y_all = np.concatenate((y_train, y_test), axis=0)
# # x_train, x_test, y_train, y_test = train_test_split(x_all, y_all, test_size=0.2, random_state=42)
# # print(x_train.shape)
# # print(x_test.shape)
# # x_train = x_train / 255.0
# # x_test = x_test / 255.0
# # x_train = x_train.reshape(-1, 28, 28, 1)  # 這邊-1是代表不確定這邊的通道數是多少
# # x_test = x_test.reshape(-1, 28, 28, 1)
# # y_train = to_categorical(y_train, num_classes=10) # 類別轉成二元陣列
# # y_test = to_categorical(y_test, num_classes=10)
#
# data_dir = "D:\download\Make_up_Dataset\Style" # "D:\download\Block_Dataset_Shape" "D:\download\Block_Dataset_Color"
#
# train_dataset = tf.keras.utils.image_dataset_from_directory(
#     data_dir,
#     labels='inferred',
#     label_mode='int',
#     image_size=(128, 128),
#     batch_size=4,
#     shuffle=True,
#     seed=123,
#     subset = 'training',
#     validation_split = 0.2
# )
# test_dataset = tf.keras.utils.image_dataset_from_directory(
#     data_dir,
#     labels='inferred',
#     label_mode='int',
#     image_size=(128, 128),
#     batch_size=4,
#     shuffle=True,
#     seed=123,
#     subset = 'validation',
#     validation_split = 0.2
# )
# print("Total images (file_paths):", len(train_dataset.file_paths))
# print(train_dataset.class_names)
# class_names = train_dataset.class_names
# print("Total images (file_paths):", len(test_dataset.file_paths))
# print(test_dataset.class_names)
#
# x_train = np.concatenate([x for x, y in train_dataset], axis=0)
# y_train = np.concatenate([y for x, y in train_dataset], axis=0)
# print(y_train)
# x_test = np.concatenate([x for x, y in test_dataset], axis=0)
# y_test = np.concatenate([y for x, y in test_dataset], axis=0)
# # print(y_test)
# print(x_train.shape)
# print(y_train.shape)
# x_train = x_train / 255.0
# x_test = x_test / 255.0
# y_train = to_categorical(y_train, num_classes=6) # 類別轉成二元陣列
# y_test = to_categorical(y_test, num_classes=6)
#
# datagen = ImageDataGenerator(
#     rotation_range=30,  # 增加旋轉範圍
#     width_shift_range=0.3,
#     height_shift_range=0.3,
#     zoom_range=0.3,
#     horizontal_flip=True,
#     brightness_range=[0.1, 1.2],  # 更大範圍的亮度調整
#     shear_range=0.3,
#     fill_mode='nearest'
# )
#
#
# # URL = "https://tfhub.dev/tensorflow/efficientnet/lite0/feature-vector/2"
# # feature_extractor = hub.KerasLayer(URL,
# #                                    trainable=False,  # 凍結參數，使參數無法被訓練
# #                                    input_shape=(128, 128, 3))
# # feature_extractor = DenseNet121(input_shape=(320, 240, 3), include_top=False)
# # feature_extractor.trainable = False
#
# # datagen.fit(x_train)
# # datagen.fit(x_test)
# # print(x_train)
#
# def block(x, filters, strides = 2, conv_short = True):
#     if conv_short:
#         short_cut = Conv2D(filters = filters, kernel_size = 1, strides = strides, padding = 'valid')(x)
#         short_cut = BatchNormalization(epsilon = 1.001e-5)(short_cut)
#     else:
#         short_cut = x
#
#     x = Conv2D(filters = filters, kernel_size = 3, strides = strides, padding = 'same')(x)
#     x = BatchNormalization(epsilon = 1.001e-5)(x)
#     x = Activation('relu')(x)
#
#     x = Conv2D(filters=filters, kernel_size=3, strides=1, padding='same')(x)
#     x = BatchNormalization(epsilon=1.001e-5)(x)
#     x = Activation('relu')(x)
#
#     x = Add()([x, short_cut])
#     x = Activation('relu')(x)
#
#     return x
#
# def Resnet(inputs, classes):
#     x = Conv2D(filters = 64, kernel_size = (7, 7), strides = (2, 2), padding = 'same', activation = 'relu')(inputs)
#     x = MaxPooling2D(pool_size = (3, 3), strides = (2, 2), padding = 'same')(x)
#     x = block(x, filters = 64, strides = 1, conv_short = False)
#     x = block(x, filters=64, strides=1, conv_short=False)
#     x = block(x, filters=64, strides=1, conv_short=False)
#
#     x = block(x, filters=128, strides=1, conv_short=True)
#     x = block(x, filters=128, strides=1, conv_short=False)
#     x = block(x, filters=128, strides=1, conv_short=False)
#     x = block(x, filters=128, strides=1, conv_short=False)
#
#     x = block(x, filters=256, strides=1, conv_short=True)
#     x = block(x, filters=256, strides=1, conv_short=False)
#     x = block(x, filters=256, strides=1, conv_short=False)
#     x = block(x, filters=256, strides=1, conv_short=False)
#     x = block(x, filters=256, strides=1, conv_short=False)
#     x = block(x, filters=256, strides=1, conv_short=False)
#
#     x = block(x, filters=512, strides=1, conv_short=True)
#     x = block(x, filters=512, strides=1, conv_short=False)
#     x = block(x, filters=512, strides=1, conv_short=False)
#
#     x = GlobalAveragePooling2D()(x)
#     x = Dense(classes, activation = 'softmax')(x)
#     return x
#
# inputs = Input(shape = (128, 128, 3))
# model = Model(inputs, Resnet(inputs = inputs, classes = 6))
# # model.summary()
# optimizer = Adam(learning_rate=0.0001)
# model.compile(optimizer=optimizer, loss = 'categorical_crossentropy', metrics = ['accuracy'])
# history = model.fit(x_train, y_train, epochs = 50, batch_size=32)
#
# # model.save('Openmv_Sensor.h5')
# test_loss, test_accuracy = model.evaluate(x_test, y_test)
# print("acc: ", test_accuracy)
# output = model.predict(x_test)
# y_pred_indices = np.argmax(output, axis=1)
# y_true_indices = np.argmax(y_test, axis=1)
# y_pred_labels = [class_names[idx] for idx in y_pred_indices]
# y_true = [class_names[idx] for idx in y_true_indices]
# print(y_pred_labels)
# print(y_true)

import cv2
from skimage.feature import hog, local_binary_pattern
from skimage import filters
import numpy as np
from scipy.stats import skew
import os
from sklearn.model_selection import train_test_split, KFold
from sklearn.svm import SVC
from sklearn.metrics import classification_report, accuracy_score
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn import neighbors
import keras
import tensorflow as tf
from tensorflow.keras.models import Sequential, Model
from tensorflow.keras.layers import Dense, Conv2D, MaxPooling2D, Flatten, Dropout, BatchNormalization, ReLU, \
    GlobalAveragePooling2D, Activation, Add, Input
from tensorflow.keras.regularizers import l1, l2
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.utils import to_categorical
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import RandomForestClassifier, ExtraTreesClassifier
from xgboost import XGBClassifier
import pickle
import gzip

base_cnn = Sequential([
    Conv2D(32, (3,3), strides=2, padding='same', activation='relu', input_shape=(320,320,3)),
    MaxPooling2D(3, padding='same'),
    Conv2D(64, (3,3), strides=2, padding='same', activation='relu'),
    MaxPooling2D(3, padding='same'),
    Conv2D(128, (3,3), strides=2, padding='same', activation='relu'),
    MaxPooling2D(3, padding='same'),
    Conv2D(256, (3,3), strides=2, padding='same', activation='relu'),
    MaxPooling2D(3, padding='same'),
    # 去掉后面的 Dense(512)
])
# 用 GlobalAveragePooling2D 或 Flatten 取出特征向量
x = base_cnn.output
x = GlobalAveragePooling2D()(x)  # → shape=(None,256)
feature_extractor = Model(inputs=base_cnn.input, outputs=x)

def extract_gabor_feats(gray, freqs=[0.1,0.3], thetas=[0, np.pi/4, np.pi/2]):
    feats = []
    for frequency in freqs:
        for theta in thetas:
            real, imag = filters.gabor(gray, frequency=frequency, theta=theta)
            feats.append(real.mean())
            feats.append(real.var())
            feats.append(imag.mean())
            feats.append(imag.var())
    return np.array(feats)  # shape = len(freqs)*len(thetas)*4

def extract_features(img):
    # 1. HOG 分析輪廓之特徵向量
    img = cv2.resize(img, (128, 128))
    # img_array = img.astype('float32') / 255.0
    # # batch 维度
    # img_batch = np.expand_dims(img_array, axis=0)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    hog_feat = hog(gray,
                   orientations=6, pixels_per_cell=(16, 16),
                   cells_per_block=(1,1), block_norm='L2-Hys')
    # print('hog', hog_feat)
    # 2. LBP 分析表面紋理
    P = 8
    lbp = local_binary_pattern(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY),
                               P=P, R=1, method='uniform')
    (hist, _) = np.histogram(lbp.ravel(),
                             bins=np.arange(0, P + 3),
                             range=(0, P + 2))
    hist = hist.astype("float")
    hist /= hist.sum()
    # print('lbp', lbp)
    # 3. 色彩矩（HSV）
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    moments = []
    for ch in cv2.split(hsv):
        moments += [np.mean(ch), np.std(ch), skew(ch.flatten())]
    # print('moments', moments)
    real, imag = filters.gabor(gray, frequency=0.6, theta=np.pi / 4)

    # gabor_feats = extract_gabor_feats(gray,
    #                                   freqs=[0.2, 0.4, 0.6],
    #                                   thetas=[0, np.pi / 4, np.pi / 2, 3 * np.pi / 4])

    # 100, 150, 250, 250
    # 300, 150, 450, 250
    # 190, 350, 400, 470

    # x, y, w, h = 190 // 2, 350 // 2, 210 // 2, 120 // 2
    # lip_roi = img[y:y + h, x:x + w]
    # # 計算色彩直方圖
    # hist_lip = cv2.calcHist([lip_roi], [0], None, [8], [0, 180])
    # cv2.normalize(hist_lip, hist_lip)
    #
    # x, y, w, h = 300 // 2, 150 // 2, 150 // 2, 100 // 2
    # eye_roi = img[y:y + h, x:x + w]
    # # 計算色彩直方圖
    # hist_eye = cv2.calcHist([eye_roi], [0], None, [8], [0, 180])
    # cv2.normalize(hist_eye, hist_eye)
    #
    # cnn_feats = feature_extractor.predict(img_batch)
    # cnn_feats = cnn_feats.flatten()

    feat = np.hstack([hog_feat, hist, moments, real.mean(),
                      ]) # hist_lip.flatten().tolist(), hist_eye.flatten().tolist(), cnn_feats
    print(feat.shape)
    return feat


data, labels = [], []
color_dirs = {'Japanese':"D:\download\Make_up_Dataset\Style\Japanese",
              'Korean':"D:\download\Make_up_Dataset\Style\Korean", 'Weatern':"D:\download\Make_up_Dataset\Style\Weatern"}
# 'Chinese':"D:\download\Make_up_Dataset\Chinese",
cnt = 0
for label, d in color_dirs.items():
    for fname in os.listdir(d):
        cnt += 1
        img = cv2.imread(os.path.join(d, fname))
        feature = extract_features(img)
        data.append(feature)
        labels.append(label)
        print(cnt)

        # features = []
        # features.append(feature)
        #
        # with gzip.open("D:\\pythonProject\\xgboost_makeup", 'r') as f:
        #     xgboostModel = pickle.load(f)
        #     pred = xgboostModel.predict(np.array(features))
        #     print(pred)

# temp_data = pd.DataFrame(data = data)
# corr = temp_data.corr("pearson")
# fig, ax = plt.subplots(figsize = (15, 15))
# sns.heatmap(corr, cmap = 'RdBu', annot = True)
# plt.show()

le = LabelEncoder()
labels = le.fit_transform(labels)

print(np.array(data).shape)
x_train, x_test, y_train, y_test = train_test_split(data, labels, random_state=42)
scale = StandardScaler()
x_train = scale.fit_transform(x_train)
x_test = scale.transform(x_test)
x_train = np.array(x_train, dtype=np.float32)
y_train = np.array(y_train, dtype=np.float32)
x_test = np.array(x_test, dtype=np.float32)
y_test = np.array(y_test, dtype=np.float32)
print(np.array(x_train).shape)
print(np.array(y_train).shape)

# KNNclf = neighbors.KNeighborsClassifier(n_neighbors=18,
#                                                  weights='distance',
#                                                  algorithm='auto',
#                                                  leaf_size=30,
#                                                  p=2,
#                                                  metric='euclidean',
#                                                  metric_params=None,
#                                                  n_jobs=None)
# KNNclf.fit(x_train, y_train)
# print(classification_report(y_test, KNNclf.predict(x_test)))
# print(accuracy_score(y_test, KNNclf.predict(x_test)))

xgbclf = XGBClassifier(learning_rate = 0.1,
                      n_estimators = 100,
                      max_depth = 3,
                      min_child_weight = 1,
                      gamma = 0,
                      subsample = 1,
                      colsample_bytree = 1,
                      scale_pos_weight = 1,
                      random_state = 27,
                      verbosity = 0,
                      booster = 'gbtree',
                      n_jobs = 1,
                      max_delta_step = 0,
                      colsample_bylevel = 1,
                      colsample_bynode = 1,
                      base_score = 0.5)
xgbclf.fit(x_train, y_train)
print(classification_report(y_test, xgbclf.predict(x_test)))
print(accuracy_score(y_test, xgbclf.predict(x_test)))

with gzip.GzipFile('xgboost_makeup', 'w') as f:
    pickle.dump(xgbclf, f)

extraclf = ExtraTreesClassifier(n_estimators=100,
                                  n_jobs=None,
                                  criterion='gini',
                                  max_depth=None,
                                  min_samples_split=2,
                                  max_features='sqrt',
                                  min_weight_fraction_leaf=0.0,
                                  min_samples_leaf=1)
extraclf.fit(x_train, y_train)
print(classification_report(y_test, extraclf.predict(x_test)))
print(accuracy_score(y_test, extraclf.predict(x_test)))

clf_RF = RandomForestClassifier(n_estimators=100,
                                      n_jobs=-1,
                                      criterion='gini',
                                      max_depth=None,
                                      min_samples_split=2,
                                      max_features='sqrt',
                                      min_samples_leaf=5,
                                      random_state = 42,
                                      bootstrap=True,
                                      oob_score=True)
clf_RF.fit(x_train, y_train)
print(classification_report(y_test, clf_RF.predict(x_test)))
print(accuracy_score(y_test, clf_RF.predict(x_test)))

clf = SVC(kernel='linear', probability=True)
clf.fit(x_train, y_train)
print(classification_report(y_test, clf.predict(x_test)))
print(accuracy_score(y_test, clf.predict(x_test)))

y_train_1 = xgbclf.predict_proba(x_train)[:, 1]  # 用 predict_proba 而非 predict
y_train_2 = extraclf.predict_proba(x_train)[:, 1]
y_train_3 = clf_RF.predict_proba(x_train)[:, 1]
y_train_4 = clf.predict_proba(x_train)[:, 1]

y_test_1 = xgbclf.predict_proba(x_test)[:, 1]
y_test_2 = extraclf.predict_proba(x_test)[:, 1]
y_test_3 = clf_RF.predict_proba(x_test)[:, 1]
y_test_4 = clf.predict_proba(x_test)[:, 1]

kf = KFold(n_splits=5, shuffle=True, random_state=42)
meta_train = np.zeros((len(x_train), 4))

for train_idx, val_idx in kf.split(x_train):
    x_tr, x_val = x_train[train_idx], x_train[val_idx]
    y_tr, y_val = y_train[train_idx], y_train[val_idx]

    xgbclf.fit(x_tr, y_tr)
    extraclf.fit(x_tr, y_tr)
    clf_RF.fit(x_tr, y_tr)
    clf.fit(x_tr, y_tr)

    meta_train[val_idx, 0] = xgbclf.predict_proba(x_val)[:, 1]
    meta_train[val_idx, 1] = extraclf.predict_proba(x_val)[:, 1]
    meta_train[val_idx, 2] = clf_RF.predict_proba(x_val)[:, 1]
    meta_train[val_idx, 3] = clf.predict_proba(x_val)[:, 1]

meta_test = np.column_stack([y_test_1, y_test_2, y_test_3, y_test_4])  # 將測試集的預測結果拼接

model = Sequential()
# model.add(Dense(16, input_shape=(31, ))) #24/30
# model.add(BatchNormalization())
# model.add(ReLU())

model.add(Dense(32, input_shape=(3, )))
# model.add(BatchNormalization())
model.add(ReLU())

# model.add(Dense(32,kernel_regularizer=l2(1e-5)))
# model.add(BatchNormalization())
# model.add(ReLU())

# model.add(Dense(64,kernel_regularizer=l2(1e-5)))
# model.add(BatchNormalization())
# model.add(ReLU())
#
# model.add(Dense(128,kernel_regularizer=l2(1e-5)))
# model.add(BatchNormalization())
# model.add(ReLU())

model.add(Dense(256))
# model.add(BatchNormalization())
model.add(ReLU())

# model.add(Dense(512))
# model.add(BatchNormalization())
# model.add(ReLU())

model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dense(4, activation='softmax'))

y_train = to_categorical(y_train, num_classes=4) # 類別轉成二元陣列
y_test = to_categorical(y_test, num_classes=4)

optimizer = Adam(learning_rate=0.001)
model.compile(optimizer=optimizer, loss = 'categorical_crossentropy', metrics = ['accuracy'])
history = model.fit(meta_train, y_train, batch_size=32, epochs = 200,
                    validation_data=(meta_test, y_test)) # 50/

# model.save('Openmv_Sensor_Shape.h5')
total_loss, test_accuracy = model.evaluate(meta_test, y_test)
print("acc: ", test_accuracy)
class_preds = model.predict(meta_test)
y_pred_indices = np.argmax(class_preds, axis=1)
y_true_indices = np.argmax(y_test, axis=1)
class_names = ['Japanese', 'Korean', 'Weatern']
y_pred_labels = [class_names[idx] for idx in y_pred_indices]
y_true = [class_names[idx] for idx in y_true_indices]
print(y_pred_labels)
print(y_true)