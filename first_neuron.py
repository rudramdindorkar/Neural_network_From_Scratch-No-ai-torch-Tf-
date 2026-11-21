#This file is just form nureon understanidng and basics for me 
inputs=[1,2,3]#repressting weights and inpusts as list
weights=[0.1,0,2,0.3]
bais=7 #bais is a additnal learnable parameter 

output=(inputs[0]*weights[0]+inputs[1]*weights[1]+inputs[2]*weights[2]+bais)
print(output)#13.1 output of a single neuron is weighted sum of its input and bais 