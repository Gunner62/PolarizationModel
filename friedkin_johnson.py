import random
import matplotlib.pyplot as plt
from matplotlib import animation
import numpy as np
# import seaborn as sns
import unittest

N = 20**2                               #input number of agents 
n = int(np.sqrt(N))                                
time = 500                                 #input desired length of sim
T = np.linspace(0, (time-1), time)         #time space

#print(T)
#print('')

def opn_ass(l,u,N,x):                        #opinion assigner - lower/upper bounds
    for i in range(N):                       #number of agents, empty array
        x.append(random.uniform(l,u))

x=[]
l = 0
u = 100
for i in range(N):
        x.append(random.uniform(l,u))
x_copy = x.copy()

a = np.random.dirichlet(np.ones(N), size=N)
g = np.random.random_sample((N,N))
identity = np.identity

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






print(x)
print(x_copy)
#print(a)
print('')
#
#func(1,N,x_copy)
#x_copy = x.copy()
#if x == butt:
#    print('x =/= butt')
#else:
#    print('x changed')
#print('')
#
print(x)
print(x_copy)
#print(a)
print('')
#
#func(1,N,x_copy)
#x_copy = x.copy()
#if x == butt:
#    print('x =/= butt')
#else:
#    print('x changed')
#print('')
#
#
#print(len(x))
print(x)
print(x_copy)
print('')


#class TestingEquality(unittest.TestCase):
 #   def test_equal(x_copy):
  #      x_copy.assertEqual = () 

#==============================================================================
# ANIMATION EXAMPLE
#==============================================================================
# First set up the figure, the axis, and the plot element we want to animate
#fig = plt.figure()
#ax = plt.axes(xlim=(0, 2), ylim=(-2, 2))
#line, = ax.plot([], [], lw=2)

# initialization function: plot the background of each frame
def init():
    line.set_data([], [])
    return line,

# animation function.  This is called sequentially
def animate(i):
    x = np.linspace(0, 2, 1000)
    y = np.sin(2 * np.pi * (x - 0.01 * i))
    line.set_data(x, y)
    return line,

# call the animator.  blit=True means only re-draw the parts that have changed.


###anim = animation.FuncAnimation(fig, animate, init_func=init,
                               #frames=200, interval=20, blit=True)

# save the animation as an mp4.  This requires ffmpeg or mencoder to be
# installed.  The extra_args ensure that the x264 codec is used, so that
# the video can be embedded in html5.  You may need to adjust this for
# your system: for more information, see
# http://matplotlib.sourceforge.net/api/animation_api.html
#anim.save('basic_animation.mp4', fps=30, extra_args=['-vcodec', 'libx264'])

###plt.show()
#==============================================================================
# HEATMAP EXAMPLE
#==============================================================================
#fig, ax_lst = plt.subplots(1, 1)
#ax_lst = ax_lst.ravel()

def plot(data):
    data = np.random.rand(10, 10)
    heatmap = ax_lst.pcolor(data)

####ani = animation.FuncAnimation(fig, plot, interval=1)
####plt.show()
#==============================================================================

fig, ax_lst = plt.subplots(1,1)

i = 0
def anal(i):
    x_copy = x.copy()
    data = func(i,N,x_copy)
    x_copy = x.copy()
#    print(i)
#    print(func(i,N))
#    print('')
#    i += 1    
    heatmap = ax_lst.pcolor(data, vmin=l, vmax=u)
    #fig.colorbar(heatmap, ax_lst)

ani = animation.FuncAnimation(fig, anal, frames=200, interval=150)

plt.show()
