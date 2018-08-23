from matplotlib import pyplot as plt

x=[78.7, 78.7, 84.5, 84.5]

x2=[78.7, 78.7, 86.8, 86.8]

y= [1200, 1600, 1600, 1200]

y2= [1200, 1800, 1800, 1200]

gross = (85.45, 1800)
aerobatic = [83.3, 1573]


plt.plot(x,y,'b-.')
plt.plot(x2,y2,'b') 
plt.xlabel('Aircraft C of G - [Inch]')
plt.ylabel('Aircraft Weight - [lbs]')
plt.title('Centre of Gravity Limits')
plt.plot(85.45, 1800, 'bo')
plt.plot(83.3, 1573,'b+')
plt.grid()
plt.show()
