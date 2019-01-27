# PolarizationModel

The models used in this program have been taken from: "Opinion Dynamics and
Bounded Confidence Models, Analysis, and Simulation" by Rainer Hegselmann 
and Ulrich Krause (2002).

In this program we aim to simulate different models of opinion formation 
within an interacting population. We consider each individual, or *agent*, in 
the population to have some *opinion* between 0 and 1 which they update based 
on the opinions of all other agents in the population. To normalize this
updating each agent has a *weight* associated with all other agents such that
their sum is 1. With this model as a baseline, we add complexity to create 3 
more models:
1. Social susceptibility model
2. Bounded confidence model
3. Bounded confidence and proximity model

blah
