import random

d1 = random.Random()
d2 = random.Random()

rolls = []
duplo = 0
for i in range (10) :
  a = d1.randrange(1,7)
  b = d2.randrange(1,7)
  rolls.append ([a,b])
  print(a,b)
  if a + b == 12 :
    duplo = duplo + 1
    print ('Duplo seis!')
    

print(rolls)
print (duplo)