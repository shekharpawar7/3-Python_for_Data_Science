#matplotlib

import matplotlib.pyplot as plt
plt.plot([13,5,65,24,86,23,99])



import numpy as np
x=np.arange(1,4)
plt.plot=(x)
plt.show()


import matplotlib.pyplot as plt
plt.plot([1,2,3,4,5,6])
plt.show()

#.................................................................................
#multiline plot
import matplotlib.pyplot as plt
x= range(1,5)
plt.plot([xi*2 for xi in x])
plt.plot([xi*4 for xi in x])
plt.plot([xi/2 for xi in x])
plt.show()

#......................................................................
import matplotlib.pyplot as plt
import numpy as np
#adding grid
x=np.arange(1,5)
plt.plot( x,x*1.5 , x,x*3.0 , x, x/3.0)
plt.grid(True)

#..............................................................................
#chnage axis
import matplotlib.pyplot as plt
import numpy as np
x=np.arange(1,6)
plt.plot(x,x*3,  x,x*6 , x,x/3)
plt.axis([0,5,-1,13]) #[xmin,nmax,ymin,ymax]

#...................................................................................
#add lebale
import matplotlib.pyplot as plt
plt.plot([13,5,65,24,86,23,99])
plt.xlabel("this is a X axis")
plt.ylabel("this is a Y axis")

#..............................................................................
#add tittle
import matplotlib.pyplot as plt
plt.plot=([17,32,65,24,13])
plt.show()

