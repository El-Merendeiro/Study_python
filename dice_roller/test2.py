import random
x = int(input ("x"))
y = int(input ("y"))
possibili = []

for t in range (1,y+1):
  possibili += [t]

result = [random.choice (possibili) for _ in range (x)]
print (possibili)
print (result)
massimo = result[0]
for n in result:
  print (n)
  if n > massimo:
    massimo = n
print (massimo)

