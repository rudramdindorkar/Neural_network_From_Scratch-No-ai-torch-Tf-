#making a nn with 2 hidden layer 
#arch=inputs ->4 neurons-> 2 neuron-> one output
import numpy as np

x=[1,2,3]

w1=[
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0.1,0.2,0.3]
]
b1=[12,12,12,12]

w2=[
    [3,1,4,5],
    [8,9,12,32]
]
b2=[11,11]

w3=[45,0]


b3=4

H1=np.dot(w1,x)+b1

H2=np.dot(w2,H1)+b2

output=np.dot(w3,H2)+b3


print("hidden layer 1",H1)
print("Hidden layer 2 ",H2)


print("output",output)


