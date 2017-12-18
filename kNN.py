from numpy import *
import operator #运算符模块

def createDataSet():
    group = array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    labels = ['A','A','B','B']
    return group,labels

def classify0(inX,dataSet,labels,k):
    """
    :param inX: 等待分类的数据向量
    :param dataSet: 样本数据向量数组
    :param labels: 样本数据对应的标签数组
    :param k: 取近邻个数
    :return:
    """
    dataSetSize = dataSet.shape[0]#获得第一个维度的个数，这里就是样本数据的条数
    #print(dataSetSize)4  array.shape (4,4)
    diffMat = tile(inX,(dataSetSize,1)) - dataSet#构造一个输入向量与每个样本数据向量的差值的list
    """diffMat
    [[-1.  -1.1]
    [-1.  -1. ]
    [ 0.   0. ]
    [ 0.  -0.1]]
    """
    sqDiffMat = diffMat**2#直接对矩阵中每个元素做了操作
    """sqDiffMat
    [[ 1.    1.21]
    [ 1.    1.  ]
    [ 0.    0.  ]
    [ 0.    0.01]]
    """
    sqDistances = sqDiffMat.sum(axis=1) #将矩阵中每行做和
    distances = sqDistances**0.5 #到这实现了输入向量与样本向量求距离，每行存储着距离
    #print(distances)[ 1.48660687  1.41421356  0.          0.1       ]
    sortedDistIndicies = distances.argsort()
    #print(sortedDistIndicies)得到原数组排序的索引[2 3 1 0]
    classCount={}
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel,0)+1
        #sortedClassCount = sorted(classCount.__iter__(),key=operator.itemgetter(1),reverse=True)
        #return sortedClassCount[0][0]

