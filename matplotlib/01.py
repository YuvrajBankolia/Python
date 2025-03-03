import matplotlib.pyplot as plt 
import numpy as np

# x= ["python" , "cpp" , "java"]
# y =[90 ,45,43]
# colors = ['r','b','y']
# plt.barh(x,y,color = colors)
# plt.title("plot")
# plt.show()

# labels = ['category A ' , ' category B ' , 'category C']
# sizes = [25 , 60,15]
# colors = ['r' , 'g' , 'b' ]
# plt.pie(sizes, labels = labels, colors= colors)
# plt.title("pie chart")
# plt.show()

# x= ["python" , "cpp" , "java"]
# y =[50,60,70]
# size = [ 450,700,340]
# plt.scatter(x,y , s =size ,alpha=0.99 , marker="*" , edgecolors="black")

# plt.title("scatter plot" )
# plt.show()

# x = [1,2,3,4,5]
# y1 = [10,11,12,13,14]
# y2 = [0,10,20,30 , 40]
# plt.fill_between(x , y1,y2,color='blue')
# plt.show()

# x= [1,2,3,4]
# y=[5,6,7,8]
# plt.grid()
# plt.step(x,y,marker = "*")
# plt.show()









x = [ 4,7,3,8]
y =[ 3,7,2,21]
plt.subplot(2,2,1)
# plt.pie(10 , 80 , 10)
plt.plot(x,y,color = 'blue')
# plt.show()

plt.subplot(2,2,2)
# plt.pie(10 , 80 , 10)
plt.pie(x)
# plt.show()

plt.subplot(2,2,3)
data = np.random.randn(1000)
plt.hist(data , bins =30 , edgecolor = 'black')
plt.title("histogram")
# plt.pie(10 , 80 , 10)
# plt.plot(x,y,color = 'blue')

plt.subplot(2,2,4)
# plt.pie(10 , 80 , 10)
plt.plot(x,y,color = 'blue')

plt.subplots_adjust(hspace = 0.6)
plt.subplots_adjust(wspace =0.6)

plt.show()






