import tensorflow as tf
import random
from keras.models import load_model
from keras import layers
from keras.callbacks import ReduceLROnPlateau
from keras import optimizers
from keras.optimizers import RMSprop
from sklearn.cross_validation import train_test_split
from keras.models import Sequential, Model
from keras.layers import Input, Add, Dense, Activation, ZeroPadding2D, BatchNormalization, Flatten, Conv2D, AveragePooling2D, MaxPooling2D, GlobalMaxPooling2D
from keras.layers.convolutional import Conv2D
from keras.layers import  MaxPool2D
from keras.layers import  Softmax, Dropout, Flatten
from keras.initializers import glorot_uniform
import pandas as pd
import numpy as np
import glob
from sklearn import metrics
import pylab as pl
import matplotlib.pyplot as plt
from pandas import DataFrame

np.set_printoptions(threshold=np.nan)

#*************************************jupyter_notebook*****************************************




pos_path = 'positive_test/*_learn_aa1000_0.4.txt'
neg_path = 'neg_cross/*_learn_aa1000_0.4.txt'



pos_num = len(glob.glob(pos_path))
neg_num = len(glob.glob(neg_path))

print("pos_num", pos_num)
print("neg_num", neg_num)


col_size=125
row_size=1000
pos_samples = np.zeros((pos_num, row_size, col_size))
pos_labels = np.ones(pos_num)

neg_samples = np.zeros((neg_num, row_size, col_size))
neg_labels = np.zeros(neg_num)


index=0
for name in glob.glob(pos_path):
    print(name)
    t2=loadSplit(name)
    pos_samples[index,:,:] = t2
    index=index+1

index=0
for name in glob.glob(neg_path):
    print(name)
    t2=loadSplit(name)
    neg_samples[index,:,:] = t2
    index=index+1


pos_samples, pos_labels = randomShuffle(pos_samples, pos_labels)
neg_samples, neg_labels = randomShuffle(neg_samples, neg_labels)

X_test = np.vstack((pos_samples, neg_samples))
Y_test = np.hstack((pos_labels, neg_labels))
X_test, Y_test = randomShuffle(X_test, Y_test)


X_test = X_test.reshape(X_test.shape[0],  row_size, col_size, 1)
Y_test = Y_test.reshape(Y_test.shape[0],  1)

	

def aucFigureS(label, pred, name):

    fpr, tpr, thresholds = metrics.roc_curve(label, pred, pos_label=1)
    auc = metrics.auc(fpr, tpr)
    model_name="DeepBindRG"
    plt.plot(fpr, tpr, lw = 1, label = 'auc(%.4f)' % auc)
    plt.xlim([-0.05, 1.05])
    plt.ylim([-0.05, 1.05])
    plt.legend(loc = 'best')
    pl.title("ROC curve of %s" % model_name)
    pl.xlabel("False Positive Rate")
    pl.ylabel("True Positive Rate")
    #plt.show()
    plt.plot([0,1],[0,1],'--', color=(0.6,0.6,0.6), label='luck')
    plt.savefig(name)




model = load_model('model_resnet_n_epoch20_drop20.h5')
la=model.evaluate(x = X_test, y = Y_test)
pred = model.predict(X_test)
pred = pred.flatten()

aucFigureS(Y_test, pred, 'test.png')

auc = aucJ(Y_test, pred)

print('auc: ', auc)


print('test:')
threshold = 0.5
pred[pred > threshold] = 1
pred[pred <= threshold] = 0
print('loss and accuracy', la)

pos_index = pred == 1
pos_index = pos_index.flatten()
TPR = np.sum(Y_test[pos_index] == 1) * 1.0 / np.sum(Y_test)
print("TPR: ", TPR)

TPR = np.sum(Y_test[pos_index] == 1) * 1.0 / np.sum(pred)
print("precision: ", TPR)


print('length of pred: ', len(pred))
print('number of pos_pred: ', np.sum(pos_index))
print('number of correct pos_pred', np.sum(Y_test[pos_index] == 1))


print("pos_num", pos_num)
print("neg_num", neg_num)





