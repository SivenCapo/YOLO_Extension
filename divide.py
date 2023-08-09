import os
import random

trainval_percent = 0.9
train_percent = 0.9
xmlfilepath = './datasets/Annotations'  # 数据集位置
txtsavepath = './datasets/images'  # 图片位置
tmage_sets_path = './datasets/ImageSets'  # 将数据集分为 训练数据集和测试数据集进行存放的位置
total_xml = os.listdir(xmlfilepath)

num = len(total_xml)
list = range(num)
tv = int(num * trainval_percent)
tr = int(tv * train_percent)
trainval = random.sample(list, tv)
train = random.sample(trainval, tr)

# 先找ImageSets文件夹如果不存在则创建
if not os.path.exists(tmage_sets_path):
    os.makedirs(tmage_sets_path)

ftrainval = open('datasets/ImageSets/trainval.txt', 'w')  # 以只写方式打开文件。如果文件存在会被覆盖。如果文件不存在，创建新文件
ftest = open('datasets/ImageSets/test.txt', 'w')
ftrain = open('datasets/ImageSets/train.txt', 'w')
fval = open('datasets/ImageSets/val.txt', 'w')

for i in list:
    name = total_xml[i][:-4] + '\n'
    if i in trainval:
        ftrainval.write(name)
        if i in train:
            ftrain.write(name)
        else:
            fval.write(name)
    else:
        ftest.write(name)

ftrainval.close()
ftrain.close()
fval.close()
ftest.close()
