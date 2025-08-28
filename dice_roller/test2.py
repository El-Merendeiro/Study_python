import random
x = int(input ("x"))
y = int(input ("y"))
possibili = []

for t in range (1,y+1):
  possibili += [t]

result = [random.choice (possibili) for _ in range (x)]

print (possibili)
print (result)

