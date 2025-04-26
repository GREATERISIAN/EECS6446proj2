import random
g=open('C:\\Users\\natan\\counting\\pseudolocust\\tasks.csv',"w")
tasks=[]
for i in range(4):
    tasks.append(2**random.randint(0,7))
    print(tasks[i])
g.write(str(tasks))
g.close()
    
f=open("tasks.csv")
str=f.read()[1:-1]
print(str)
print(str.split(','))
