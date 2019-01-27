import random
import matplotlib.pyplot as plt
from matplotlib import animation    
import numpy as np

print("Welcome to Polarization Model Simulator")

tutorialMode = input("Do you want to use in tutorial mode? (y/n): ")

while tutorialMode != 'y' and tutorialMode != 'n':
    
    tutorialMode = input("Please input y/n: ")


if tutorialMode == 'y':
    
    print("A uniform distribution will be used for agents' inital opinions")
    print("We will use 100 agents")

    SIZE_OF_AGENTS = 100
    agentOpinions = np.linspace(0,1,SIZE_OF_AGENTS)
    epsilon = 0.15
    proximity = 5
    NUMBER_OF_TRIALS = SIZE_OF_AGENTS
    selfConfidence = np.random.rand(SIZE_OF_AGENTS)
    

else:
    SIZE_OF_AGENTS = int(input("Enter size of agents and trial (same value): "))
    NUMBER_OF_TRIALS = SIZE_OF_AGENTS
    # NUMBER_OF_TRIALS = int(input("Enter number of trials: "))
    epsilon = float(input("Enter the epsilon value: "))
    proximity = int(input("Enter the proximity value: "))
    selfConfidence = np.random.rand(SIZE_OF_AGENTS)
    
    print("Enter your option for agent opinion distribution")
    print("Option 1: Normal distribution")
    print("Option 2: Uniform distribution")
    distributionMode = int(input("Enter choice of distribution: "))
    
    if (distributionMode == 1) :
        mu = float(input("Enter mean value: "))
        sigma = float(input("Enter s.d. value: "))
        agentOpinions = np.random.normal(mu, sigma, SIZE_OF_AGENTS)
    elif (distributionMode == 2) :
        agentOpinions = np.linspace(0,1,SIZE_OF_AGENTS)


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
def generateBoundedProxMatrix(agentOpinions, epsilon, proximityLimit):
    
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
        
# agentOpinions = np.linspace(0,1,SIZE_OF_AGENTS)
aOpinions_time = np.empty((SIZE_OF_AGENTS,NUMBER_OF_TRIALS))


plt.clf()

print("1 = Simplistic Model")
print("2 = Social Susceptibility Model")
print("3 = Bounded Confidence Model")
print("4 = Bounded Confidence and Proximity Model")
modelChoice = int(input("Enter choice of model: "))

while (modelChoice != 1 and modelChoice != 2 and modelChoice != 3 and modelChoice != 4):
    
    modelChoice = int(input("Please input 1, 2, 3, or 4: "))


for n in range(NUMBER_OF_TRIALS) :

    for j in range(SIZE_OF_AGENTS) :
        aOpinions_time[j,n] = agentOpinions[j]   
    
    if modelChoice == 1:
        matrix = generateSimplisticMatrix(agentOpinions)
    
    if modelChoice == 2:
        matrix = generateSusceptibilityMatrix(agentOpinions, selfConfidence)
    
    if modelChoice == 3:
        matrix = generateBoundedMatrix(agentOpinions, epsilon)
        
    if modelChoice == 4:
        matrix = generateBoundedProxMatrix(agentOpinions, epsilon, proximity)
    
    modifyAgents(matrix, agentOpinions)

    print(agentOpinions)
    plt.plot(np.arange(n), aOpinions_time[n][:n])

#print(aOpinions_time)

plt.xlabel("Time")
plt.ylabel("Opinion")
if tutorialMode == 'y':
    plt.ylim([0,50])
else:
    plt.xlim([0,10])
plt.ylim([0,1])
plt.show()

