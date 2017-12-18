from numpy import *

# print(type(random.rand(4,4)))#<class 'numpy.ndarray'>
# print(random.rand(4,4))
#
# randMat = mat(random.rand(4,4))
# print(type(randMat))#<class 'numpy.matrixlib.defmatrix.matrix'>
# print(randMat.I)
#
# print(randMat*randMat.I-eye(4))
# print(eye(4))
#
# print(randMat*randMat.I)

import kNN

group,labels = kNN.createDataSet()
print(kNN.classify0([0,0],group,labels,3))


