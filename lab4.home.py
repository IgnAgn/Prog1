import numpy as np
import time as t

# 1. feladat

# v=np.arange(10,50)
# print(v)
# print(v[::-1])

# def visszafele(v):
#     newV=np.zeros(v.size,dtype='int32')
#     idx=0
#     for i in range(v.size-1,-1,-1):
#         newV[idx]=v[i]
#         idx+=1
#     return newV
#
# print(visszafele(v))
#
# def inverseVector(a):
#     b=np.array(a[a.size-1])
#     for i in range(a.size-2,-1,-1):
#         b=np.append(b,a[i])
#     return b
#
# print(inverseVector(v))

# 2.feladat

# v=np.random.randint(1,100,30)
# print(v)

# v=np.array(np.ceil(100*np.random.random((30))),dtype='uint8')
# minV=v.min()
# maxV=v.max()
# print(v)
# print(minV,maxV)
# ind=np.where((v==minV)|(v==maxV))
# print(ind)

# 3.feladat
#
# v=np.random.randint(1,100,30)
# print(v)
# maxV = v.max()
#
# def maxotcserel(v):
#     for i in range(0,v.size):
#         if v[i]==maxV:
#             v[i]=-1
#     return v
# print(maxV)
#
# print(maxotcserel(v))

# 4.feladat

# v=np.random.randint(1,100,100)
#
# def sortVector(v):
#     for i in range(0,v.size):
#         for j in range(i+1,v.size):
#             if v[j]<v[i]:
#                 v[i],v[j]=v[j],v[i]
#     return v
# #
# print(v)
# print(sortVector(v))

# 5.feladat

# v=np.arange(-3,15)
# v[(v<8)& (v>3)]=-1
# print(v)

# 6.feladat

# v=np.random.randint(1,100,30)
# x=int(input('number:'))
# a=np.abs(v-x)
# print(v)
# print(v[a==a.min()])

# 7.feladat
#
v=np.random.randint(-10,10,10)
def countVs(v):
    neg=0
    pos=0
    zeros=0
    for i in range(0,v.size):
        if v[i]<0:
            neg+=1
        if v[i]>0:
            pos+=1
        if v[i]==0:
            zeros+=1
    return neg,pos,zeros

print(v)
print(countVs(v))


# e = np.random.randint(1,50,150)
# print(e)
# start = t.time()
# e1 = sortVector(e)
# ended = t.time()
# print(e1)
# print('{:.15f}'.format(ended-start))