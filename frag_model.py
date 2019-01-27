import random
import matplotlib.pyplot as plt
from matplotlib import animation
import numpy as np
import seaborn as sns





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
                break;
            
            elif (boundedAgents[n] == 1):
                boundedAgents[n] = distribution[0][iterator]
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
        

agentOpinions = np.random.normal(np.ones(10), 1)
epsilon = 0.2
 
plt.hist(agentOpinions,10)
plt.show()
    

for n in range(10) :
    print(agentOpinions)
    weightMatrix = generateBoundedMatrix(agentOpinions, epsilon)
    modifyAgents(weightMatrix, agentOpinions)
    
plt.hist(agentOpinions,10)
plt.show()


#plt.hist(imalist, 5, color = "#01FF13")
#plt.ylabel("some nums")
#plt.xlabel("some stuff")
#plt.show()

