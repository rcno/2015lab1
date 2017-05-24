from scipy_setup import *

x = np.linspace(0, 10, 30)  #array of 30 points from 0 to 10
y = np.sin(x)
z = y + np.random.normal(size=30) * .2
#create new figure
plt.figure()
plt.plot(x, y, 'p-',label='A sine wave')
plt.plot(x, z, 'o-', label='Noisy sine')
plt.legend(loc = 'lower right')

# plt.xlabel("X axis")
# plt.ylabel("Y axis")

plt.savefig("sinewave.pdf")

#########Some array operations##########

print "Make a 3 row x 4 column array of random numbers"
x = np.random.random((3, 4))
print x
print

print "Add 1 to every element"
x = x + 1
print x
print

print "Get the element at row 1, column 2"
print x[1, 2]
print

# The colon syntax is called "slicing" the array. 
print "Get the first row"
print x[0, :]
print

print "Get every 2nd column of the first row"
print x[0, ::2]
print

##########Max, min and mean#######
print "Max is  ", x.max()
print "Min is  ", x.min()
print "Mean is ", x.mean()

print "Row maxima are ", x.max(axis=1)
