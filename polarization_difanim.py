import random
import matplotlib.pyplot as plt
from matplotlib import animation
import numpy as np
import seaborn as sns
import unittest

N = 20**2                               #input number of agents 
n = int(np.sqrt(N))                                
time = 500                                 #input desired length of sim
T = np.linspace(0, (time-1), time)         #time space



uniform_data = np.random.rand(10,12)
ax = sns.heatmap(uniform_data)
plt.show()







def opn_ass(l,u,N,x):                        #opinion assigner - lower/upper bounds
    for i in range(N):                       #number of agents, empty array
        x.append(random.uniform(l,u))

x=[]
l = 0
u = 100
for i in range(N):
        x.append(random.uniform(l,u))
x_copy = x.copy()

n = int(np.sqrt(N))
x_ex = [x[l:l+n] for l in range(0,len(x), n)]

a=np.random.dirichlet(np.ones(N), size=N)

#a = np.random.randn(N,N)
#a = a/(2*abs(a)) + 0.5
for j in range(N):
    for k in range(N):
        count = 0
        if a[j][k] == 1:
            count += 1
    a[j][k] = a[j][k] / count

print(a)

x_t=[]

def func(i,N,butt):
    #print(x)
    x_t = butt
    print(i)
    for i in range(i):
        for n in range(N):
            x_i = 0
            for f in range(N):
                x_i += x_t[f] * a[n][f]
            x_t[n] = x_i
    n = int(np.sqrt(N))        
    x_f = [x_t[l:l+n] for l in range(0, len(x_t), n)]
    #print(x_f)
#    if x == butt:
#        print('x =/= butt')
#    else:
#        print('x changed')
    print(x_f)
    return x_f


all_grid = []
def gen_fram(i,N,butt):                     #generate frames
    x_t = butt
    while i > 0:
        for n in range(N):
            x_i = 0
            for f in range(N):
                x_i += x_t[f] * a[n][f]
            x_t[n] = x_i
        print(i)
        i -= 1
        n = int(np.sqrt(N))
        x_f = [x_t[l:l+n] for l in range(0, len(x_t), n)]
        all_grid.append([plt.imshow(x_f,vmin=l,vmax=u)])
    return x_f


fig = plt.figure()
#fig = sns.heatmap()
gen_fram(50,N,x_copy)
#print(len(all_grid))

animate = animation.ArtistAnimation(fig, all_grid, interval=150, repeat=True)
plt.show()


#def prep_axes()


#fig, ax_lst = plt.subplots(1,1)

#i = 0
#def anal(i):
#    x_copy = x.copy()
#    data = func(i,N,x_copy)
#    x_copy = x.copy()
##    print(i)
##    print(func(i,N))
##    print('')
##    i += 1    
#    heatmap = ax_lst.pcolor(data, vmin=l, vmax=u)
#    #fig.colorbar(heatmap, ax_lst)
#
#ani = animation.FuncAnimation(fig, anal, frames=200, interval=150)
#
#plt.show()
