#This file is just for me to understand layers of neurons 
#using 3 neuron to get 3 ouptuts


inputs=[1,2,3]
weights=[[0.1,0.2,0.3], #for the purspose of understanding iam using 3 nueron and  3 inputs  
[0.4,0.5,0.6],
[0.7,0.8,0.9]]

bais=[4,5,6]
outputs=[]

# outputs = [#this method is tds to write replacing with loops
#     inputs[0]*weights[0][0] + inputs[1]*weights[0][1] + inputs[2]*weights[0][2] + bais[0],
#     inputs[0]*weights[1][0] + inputs[1]*weights[1][1] + inputs[2]*weights[1][2] + bais[1],
#     inputs[0]*weights[2][0] + inputs[1]*weights[2][1] + inputs[2]*weights[2][2] + bais[2]
# ]
for i in range (len(weights)):
    sum=0
    for j in range (len(inputs)):
        sum+=inputs[j]*weights[i][j]

    sum=sum+bais[i]
    outputs.append(sum)
print(outputs)