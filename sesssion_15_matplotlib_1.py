#Adding titles
import matplotlib.pyplot as plt
plt.plot([1,3,2,4])
plt.title('Simple plot')
plt.show()
#Matplotlib provides a simple function, plt.title() 
#to add a title

#Adding a legend
import matplotlib.pyplot as plt
import numpy as np
x=np.arange(1,5)
plt.plot(x,x*1.5,label='Normal')
plt.plot(x,x*3.0,label='Fast')
plt.plot(x,x/3.0,label='Slow')
plt.legend()
plt.show()

'''Color Abbreviation
Color Name
b blue
c cyan
g green
k black
m magenta
r red
w white
y yellow
'''
#Control colors
import matplotlib.pyplot as plt
import numpy as np
y=np.arange(1,3)
plt.plot(y,'y');
plt.plot(y+1,'m');
plt.plot(y+2,'c');
plt.show()

#Specifying styles in multiline plots
import matplotlib.pyplot as plt
import numpy as np
y=np.arange(1,3)
plt.plot(y,'y',y+1,'m',y+2,'c');
plt.show()

'''Style Abbreviation Style'''
import matplotlib.pyplot as plt
import numpy as np
y=np.arange(1,3,0.2)
plt.plot(y,'x',y+0.5,'o',y+1,'D',y+1.5,'^',y+2,'s');
plt.show()

#Histogram charts
#Histograms are used to make graphs symmetrical
import matplotlib.pyplot as plt
import numpy as np
y=np.random.randn(1000)
plt.hist(y);
plt.show()

#Bar graph is used in EDA
#Exploratory data analysis
import matplotlib.pyplot as plt
plt.bar([1,2,3],[2,3,5]);
plt.show()

'''The bar() function is used to generate bar charts 
in matplotlib'''
#Scatter plots
#Example of collinear if temp increase humidity decrease
#and viceversa
#Scatter plots are also called bivariant
#Scatter plots are collinear
import matplotlib.pyplot as plt
import numpy as np
x=np.random.randn(1000)
y=np.random.randn(1000)
plt.scatter(x,y);
plt.show()

size=50*np.random.randn(1000)
colors=np.random.randn(1000)
plt.scatter(x,y,s=size,c=colors);
plt.show

#Adding text
import matplotlib.pyplot as plt
import numpy as np
X=np.linspace(-4,4,1024)
Y=.25*(X+4.)(X+1.)(X-2.)
plt.text(-0.5,-0.25,'Brackmard minimum')
plt.plot(X,Y,c='k')
plt.show()

import seaborn as sns
import pandas
import matplotlib.pyplot as plt
#Seaborn has 18 in-built datasets,
#that can be found using the following command
sns.get_dataset_names()
df=sns.load_dataset('titanic')
df.head()

#Count plot
#hue is the attribute of countplot
sns.countplot(x='sex',data=df)
#x-The name of the column
#data-The dataframe
sns.countplot(x='sex',hue='survived',data=df,palette='Set1')
sns.countplot(y='sex',hue='survived',data=df,palette='Set2')
sns.countplot(y='sex',hue='survived',data=df,palette='Set3')

#hue- The name of the categorical column to split the bars
#palette- The color palette to be used
######################################
#KDE plot
#A kernel Density Estimate (KDE) Plot is used
#to plot the distribution of continuous data.
sns.kdeplot(x='age',data=df,color='black')

#Distribution plot
#It is histogram with KDE plot

sns.displot(x='age',kde=True,bins=6,data=df)
#kde- It is set to False by default

sns.displot(x='age',kde=True,bins=5,
hue=df['survived',palette='Set1',data=df)

################################
#scatter data set
df=sns.load_dataset('iris')
df.head()

#Scatter plots help understand co-relation between data
sns.scatterplot(x='sepal_length',y='petal_length',
data=df,hue='species')

#Join plot
sns.jointplot(x='sepal_length',y='petal_length',
data=df,kind='reg')
sns.jointplot(x='sepal_length',y='petal_length',
data=df,kind='hist')
sns.jointplot(x='sepal_length',y='petal_length',
data=df,kind='kde')

'''kind-The kind of plot to be plotted 
It can be one of yhe following.
'''
#Pair plots
sns.pairplot(df)

#Heatmap
corr=df.corr()
sns.heatmap(corr)