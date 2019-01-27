import random
import matplotlib.pyplot as plt
from matplotlib import animation
import numpy as np
import seaborn as sns





def generateSimplisticMatrix(agentOpinions):
    
    confidenceMatrix = []
    
    for i in range (len(agentOpinions)):
        distribution = np.random.dirichlet(np.ones(len(agentOpinions)), 1)
        confidenceMatrix.append(distribution[0])
        
    return confidenceMatrix


def generateSusceptibilityMatrix(agentOpinions, selfConfidence):
    
    
    confidenceMatrix = []
    
    
    for i in range (len(agentOpinions)):
        
        
        random = np.random.dirichlet(np.ones(len(agentOpinions) - 1), 1)
        distribution = (random[0]).tolist()
        distribution.insert(i, selfConfidence[i])
    
        
        for j in range (len(distribution)):
            if (j == i):
                continue
            else:
                distribution[j] = distribution[j] * (1 - selfConfidence[i])
        
        confidenceMatrix.append(distribution)
        
    return confidenceMatrix


def generateBoundedMatrix(agentOpinions, epsilon):

    confidenceMatrix = []

    for i in range (len(agentOpinions)):
        
        boundedAgents = np.zeros(len(agentOpinions)) #an array that will be 0 for xi-xj > epsilon
        validAgents = 0
        for j in range (len(agentOpinions)):
            if (np.abs(agentOpinions[i] - agentOpinions[j]) <= epsilon):
                boundedAgents[j] = 1
                validAgents += 1
        
        distribution = np.random.dirichlet(np.ones(validAgents), 1)
        iterator = 0
        
        for n in range (len(boundedAgents)):
            
            if (iterator == validAgents):
                break
            
            elif (boundedAgents[n] == 1):
                boundedAgents[n] = distribution[0][iterator]
                iterator += 1
        
        confidenceMatrix.append(boundedAgents)
        
    
    
    return confidenceMatrix
         

    #neightbour restriction
def generateBoundedMatrix(agentOpinions, epsilon, proximityLimit):
    
    confidenceMatrix = []
    
    for i in range (len(agentOpinions)):
        
        boundedAgents = np.zeros(len(agentOpinions))
        validAgents = 0
        
        if (i + proximityLimit + 1 >= len(agentOpinions)):
            startIndex = len(agentOpinions) - i - proximityLimit - 1
            endIndex = startIndex + (proximityLimit * 2) + 1
            
        else:
            startIndex = i - proximityLimit
            endIndex = i + proximityLimit + 1
        
        for x in range (startIndex, endIndex):
            if (np.abs(agentOpinions[x] - agentOpinions[i]) <= epsilon):
                boundedAgents[x] = 1
                validAgents += 1
                
        distribution = (np.random.dirichlet(np.ones(validAgents), 1))[0]
        iterator = 0
        
        for n in range (len(boundedAgents)):
            
            if (iterator == validAgents):
                break
            
            elif (boundedAgents[n] == 1):
                boundedAgents[n] = distribution[iterator]
                iterator += 1
    
        confidenceMatrix.append(boundedAgents)
    
    return confidenceMatrix
    
        
def modifyAgents(weightMatrix, agentOpinions):
    
    
    for n in range (len(agentOpinions)):
        agentOpinions[n] = getNextOpinion(weightMatrix[n], agentOpinions)
            

        
def getNextOpinion(weight, agentOpinions):
    
    nextOpinion = 0
    
    for n in range(len(agentOpinions)):
        nextOpinion += weight[n] * agentOpinions[n]
    
    
    return nextOpinion
        


agentOpinions = np.random.random(15)
#selfConfidence = np.random.random(len(agentOpinions))
epsilon = 0.2
proximity = 3


for i in range(100):
    matrix = generateBoundedMatrix(agentOpinions, epsilon, proximity)
    modifyAgents(matrix, agentOpinions)
    print(agentOpinions)


#plt.hist(imalist, 5, color = "#01FF13")
#plt.ylabel("some nums")
#plt.xlabel("some stuff")
#plt.show()

