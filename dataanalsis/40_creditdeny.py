# !/usr/bin/python3
# -*- coding:utf-8 -*-

# 构建逻辑回归分类器
# logistics回归中的Logistic函数，也称为Sigmond函数
# 使用逻辑回归对信用卡欺诈进行分类
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import itertools
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, precision_recall_curve
from sklearn.preprocessing import StandardScaler
import warnings
warnings.filterwarnings('ignore')

# 混淆矩阵可视化
def plot_confusion_matrix(cm, classes, normalize = False, title = 'Confusion matrix', cmap = plt.cm.Blues):
    plt.figure()
    plt.imshow(cm, interpolation='nearest', cmap = cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.array(len(classes))
    plt.xticks(tick_marks, classes, rotation = 0)
    plt.yticks(tick_marks, classes)

    thresh = cm.max() / 2
    for i ,j in itertools.product(cm.shape[0], range(cm.shape[1])):
        plt.text(j,i, cm[i, j],
            horizontalalignment='center',
            color = 'white' if cm[i, j] > thresh else 'black')

    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')
    plt.show()

# 显示模型评估结果
def show_metircs(cm):
    tp = cm[1,1]
    fn = cm[1,0]
    fp = cm[0,1]
    tn = cm[0,0]
    print("精确率:{:.3f}".format(tp/(tp+fp)))
    print("召回率:{:.3f}".format(tp/(tp+fn)))
    print('F1值: {:.3f}'.format(2*(((tp/(tp+fp))*(tp/(tp+fn)))/((tp/(tp+fp))+(tp/(tp+fn))))))
# 绘制精确率-召回率曲线
def plot_precision_recal():
    plt.step(recall, precision, color='p', alpha = 0.2, where = 'post')
    plt.fill_between(recall, precision ,step='post',alpha = 0.2, color = 'b')
    plt.plot(recall, presicion, linewidth=2)
    plt.xlim([0,0.1])
    plt.ylim([0,0.1,1.05])
    plt.xlabel("召回率")
    plt.ylabel("精确率")
    plt.title("精确率-召回率-曲线")
    plt.show()

# 数据加载
data = pd.read_csv('‪C:/Users/Cherry/Desktop/credit_fraud/creditcard.csv')





