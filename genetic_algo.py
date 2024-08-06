import random

def evolve(x):
    p=random.randint(1,5)
    index=random.randint(0,len(x)-1)
    if p==1:
        if x[index]==1:
            x[index]=0
        else:
            x[index]=1
        print("value changed at index",index)
    else:
        print("no changes")
    
filename=input("Enter the filename containing dna sequence:")
file=open(filename,"w")
s=input("Enter the dna sequence:")
file.write(s)
file.close()
file=open(filename,"r")
x=list(file.read())
print(x)
file.close()
for i in range(0,len(x)):
    evolve(x)
print("\nAfter Evolution\n",x,sep="")

    
