import numpy
import operator

def eucliDistance(inst1,inst2,length):
	distance = 0
	for x in range(length):
		distance += pow((inst1[x],inst2[x]),2)

	return math.sqrt(distance)


def getNeighbors(trainingSet,testInstance,k):
	distance = []
	length = len(testInstance)  #
	for x in range(len(trainingSet)):
		dist =eucliDistance(testInstance,trainingSet[x],length)
		distance.append(trainingSet[x],dist)

	distance.sort(key = operator.itemgetter(1))
	
	neighbors = []
	for x in range(k):
		neighbors.append(distance[x][0])

	return neighbors

def getResponse(neighbors):
	classVotes = {}
	for x in range(len(neighbors)):
		respnse = neighbors[x][-1]
		if response in classVotes:
			classVotes[response] += 1
		else:
			classVotes[response] = 1

	sortedVotes = sorted(classVotes.itemgetter(),key=operator.itemgetter(1),reverse = True)
	return sortedVotes[0][0]



def main():
	trainSet = [[1,1,1,'a'],[2,2,2,'a'],[1,1,3,'a'],[4,4,4,'b'],[0,0,0,'a'],[4,4.5,4,'b']]
	testInstance = [5,5,5]
	k = 6
	neighbors = getNeighbors(trainSet,testInstance,k)
	response = getResponse(neighbors)
	print "\nNeighbors Are:",
	print neighbors
	print "\nResponse is:",
	print response
