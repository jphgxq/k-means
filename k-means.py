#!/usr/bin/env python
#coding:utf-8

__author__ = 'jiapeng'

from numpy import *
import matplotlib.pyplot as plt


text = open('text.txt','wb')
#计算欧几里得距离
def euclDistance(vector1, vector2):
	return sqrt(sum(power(vector2 - vector1, 2)))

def initCentroids(dataSet, k):
	#150行 4列
	numSamples, dim = dataSet.shape
	#k行4列的零矩阵
	centroids = zeros((k, dim))
	for i in range(k):
		index = int(random.uniform(0, numSamples))
		centroids[i, :] = dataSet[index, :]
	return centroids

def kmeans(dataSet, k):
	#总行数
	numSamples = dataSet.shape[0]
	#创建150行4列零矩阵
	clusterAssment = mat(zeros((numSamples, 4)))
	clusterChanged = True
	#k行4列的矩阵
	centroids = initCentroids(dataSet, k)

	while clusterChanged:
		clusterChanged = False
		for i in xrange(numSamples):
			minDist  = 100000.0
			minIndex = 0
			for j in range(k):
				distance = euclDistance(centroids[j, :], dataSet[i, :])

				if distance < minDist:
					minDist  = distance
					minIndex = j

			if clusterAssment[i, 0] != minIndex:
				clusterChanged = True
				clusterAssment[i, :] = minIndex, minDist**2, minDist**2, minDist**2

		for j in range(k):
			pointsInCluster = dataSet[nonzero(clusterAssment[:, 0].A == j)[0]]
			centroids[j, :] = mean(pointsInCluster, axis = 0)

	print 'Congratulations, cluster complete!'
	return centroids, clusterAssment

def showCluster(dataSet, k, centroids, clusterAssment):
	numSamples, dim = dataSet.shape

	list1 = []
	list2 = []
	list3 = []
	list4 = []
	list5 = []
	for i in xrange(numSamples):
		markIndex = int(clusterAssment[i, 0])
		if markIndex == 0:
			list1.append([dataSet[i, 0],dataSet[i, 1],dataSet[i, 2],dataSet[i, 3]])
		if markIndex == 1:
			list2.append([dataSet[i, 0],dataSet[i, 1],dataSet[i, 2],dataSet[i, 3]])
		if markIndex == 2:
			list3.append([dataSet[i, 0],dataSet[i, 1],dataSet[i, 2],dataSet[i, 3]])
		if markIndex == 3:
			list4.append([dataSet[i, 0],dataSet[i, 1],dataSet[i, 2],dataSet[i, 3]])
		if markIndex == 4:
			list5.append([dataSet[i, 0],dataSet[i, 1],dataSet[i, 2],dataSet[i, 3]])
	printdata(list1)
	printdata(list2)
	printdata(list3)
	printdata(list4)
	printdata(list5)

def printdata(lst):
	for per in lst:
		text.write(repr(per) +'\n')
	text.write('='*50 +'\n')

dataSet = []
fileIn = open(r'testSet.txt')
for line in fileIn.readlines():
	lineArr = line.strip().split(' ')
	dataSet.append([float(lineArr[0]), float(lineArr[1]), float(lineArr[2]), float(lineArr[3])])
dataSet = mat(dataSet)
k = 5
centroids, clusterAssment = kmeans(dataSet, k)
showCluster(dataSet, k, centroids, clusterAssment)
text.close()