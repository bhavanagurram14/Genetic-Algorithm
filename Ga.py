#Genetic Algorithm which returns x and y co-ordinates at which the function f(x,y) gives maximum value
import random
import math


list_name = []
maxpsFitness = 0
flag_variable = 0
flag2 = 0
maximum = 0

def fun(element):
	return element[0]

#this function computes the fitness and returns it

def Fitness( x , y ):
	a=math.exp(-(x**2)-(y+1)**2)
	b=math.exp(-(x**2)-(y**2))
	c=math.exp(-(x+1)**2-(y**2))
	z=((3*(1-x)**2)*a)-((10*((x/5)-x**3-y**5))*b)-((1/3)*c)
	return z

#to generate 20 chromosomes randomly, here the x and y values are integers between 0 to 255

for i in range(20):

	x = random.randrange(0,255,1)
	y = random.randrange(0,255,1)
	list_name.append([x,y])

print('\n')

print(' Co-ordinates are')
print(list_name)
"""for i in list_name:
	print(i)"""


#this function iterates for 20 times , after that is asks the user if they still want to iterate it further.

def ga_iteration(list_name,maxpsFitness,flag_variable,xxx,yyy,flag2,maximum):
	if maxpsFitness > maximum :
		maximum = maxpsFitness
	flag2 = flag2+1
	x7 = xxx
	y7 = yyy
	m1 = maxpsFitness
	flag_variable = flag_variable + 1
	fitness=[]
	chromo=set()
	newList = []
	cmfList = []
	ps40Set = set()
	ps40Binary = set()
	ps40BinaryList =[]
	ps60Binary = set()
	ps60BinaryList = []
	cross60 = []
	psAfterCrossing = []
	psAfterMutation = []
	psFitness = []
	psFitnessXYZ = []
	
#to generate chromosomes in binary
	
	for i in list_name :
		k = format(i[0],'08b') + format(i[1],'08b')
		chromo.add(k)

	print('\n')

	"""print('Population in bitString')
	print(chromo)"""

#the chromosomes here are converted and thus represented on a real number line between -3 and +3

	for i in list_name:

		x1 = i[0]
		y1 = i[1]
	
		x = (-3) + x1*(6/255)
		y = (-3) + y1*(6/255)
	

#the fitness function is called by sending x and y values as parameters 
		z = Fitness(x,y)
#the fitness values are stored in a list called fitness
		fitness.append(z)
	
	cmf = 0
#the cumulative frequencies are calculated 
	for i in fitness:
		cmf = cmf + i
		#print(i)
	j = min(fitness)
	#print('min is')
	#print(j)

	#print('cmf is')
	#print(cmf)

	b = cmf - 20*j
	#print(b)
	"""print('list_name is ')
	print(list_name)"""
	for i in list_name:

		x1 = i[0]
		y1 = i[1]
		cr = format(x1,'08b') + format(y1,'08b')
	
		x = (-3) + x1*(6/255)
		y = (-3) + y1*(6/255)
	

		a=math.exp(-(x**2)-(y+1)**2)
		b=math.exp(-(x**2)-(y**2))
		c=math.exp(-(x+1)**2-(y**2))
		z=((3*(1-x)**2)*a)-((10*((x/5)-x**3-y**5))*b)-((1/3)*c)
	

	
		newList.append([z-j, x , y,cr])

	newList.sort(key = fun)

	print('\n')

	"""print('newList with  fitnessvalue,x co-ordinate,y co-ordinate')
	print('\n')
	for i in newList :
		print(i)"""


	k = 0
	for i in newList :
		k = k + i[0]
		cmfList.append(k)

	print('\n')

	"""print('cmf List is')
	print(cmfList)"""




	#print('ps40Set is')

	rand_number = random.uniform(0.0,b)	

#we probablisticly select 40% of the chromosomes by using the roulette wheel concept

	while len(ps40Set)<8:
		j = 0			
		for i in cmfList :
			j = j+1
			if rand_number > i :
				if rand_number < cmfList[j] :
					m = i
					n = cmfList[j+1]
					g = cmfList[j] - i
					ps40Set.add(g)
					rand_number = random.uniform(n,b)
				

					
	#print(ps40Set)
	#print(len(ps40Set))

	newListLength = len(newList)
	#print('newListLength is')
	#print(newListLength)

	for i in ps40Set :
		for j in range(0,newListLength) :
			#print(i,j)
			if i == newList[j][0] :
				ps40Binary.add(newList[j][3])
				ps40BinaryList.append(newList[j][3])
			


	"""print('ps40Binary is')
	print(ps40Binary)
	print('ps40BinaryList is')
	print(ps40BinaryList)"""
			
	ps60Binary = chromo - ps40Binary

	"""print('ps60Binary is')
	print(ps60Binary)"""

	for i in ps60Binary :
		ps60BinaryList.append(i)

	"""print('ps60BinaryList is')
	print(ps60BinaryList)"""



#the remaining 60% of chromosomes are gone through cross-over, here we have done one-point cross-over

	ps60len = len(ps60BinaryList)
	for i in range(0,ps60len,2) :
		if (i+1)<ps60len :
			a = ps60BinaryList[i]
			b = ps60BinaryList[i+1]
			bitLen = len(a)
			r = random.randrange(0,bitLen,1)

			c = a[0:r+1] + b[(r+1):bitLen]
			d = b[0:r+1] + a[(r+1):bitLen]
			cross60.append(c)
			cross60.append(d)
		else:
			psAfterCrossing.append(ps60BinaryList[i])
	
	"""print('cross60 is')
	print(cross60)"""

	print('\n')

	#print('After Crossing, ps is ')

	for i in ps40BinaryList :
		psAfterCrossing.append(i)

	for i in cross60 :
		psAfterCrossing.append(i)


	#print(psAfterCrossing)

	print('\n')

	print(' After Mutation, ps is ')

#the probability for mutation is set to 1%

	for i in psAfterCrossing :

		if ( random.randrange(0,99,1) == 2 ) :
			rand = random.randrange(0,15,1)
			if (i[rand] == 1 ):
				i[rand] == 0
			else :
				i[rand] == 1
		psAfterMutation.append(i)

	print(psAfterMutation)
	list_name = []
	for i in psAfterMutation :
		xx = (-3) + ((int(i[0:8],2))*(6/255))
		yy = (-3) + ((int(i[8:16],2))*(6/255))
		#print(xx,yy)
	
		list_name.append([int(i[0:8],2),int(i[8:16],2)])
	
		zz = Fitness(xx,yy)
		psFitness.append(zz)
		psFitnessXYZ.append([xx,yy,zz])
	#print(list_name)
	"""print('psFitness is')
	print(psFitness)"""

	print('Maximum fitness is ')

	maxpsFitness = max(psFitness)
	print(maxpsFitness)
	l1 = list_name 
	

	for i in psFitnessXYZ :
		if max(psFitness) == i[2] :
			xxx = i[0]
			yyy = i[1]	
			#print([xxx,yyy])
	if flag2 <= 200 :
		ga_iteration(l1,maxpsFitness,flag_variable,xxx,yyy,flag2,maximum)

	else :
		if m1 < maxpsFitness :
			ga_iteration(l1,maxpsFitness,flag_variable,xxx,yyy,flag2,maximum)
		else :
			print('\n')
			print('After')
			print(flag_variable - 1)
			print('Iterations we get the maximum fitness')
			print('\n')
			print('Value is')
			print(m1)
			print('\n')
			print('co-ordinates are')
			print([x7,y7])
			print("Maximum fitness till now is ",maximum)
			print('Do you want to go for another iteration ?? yes/ no ')
			string = input()
			if ( string == 'yes'):
				ga_iteration(l1,maxpsFitness,flag_variable,xxx,yyy,flag2,maximum)
			else :
				return
	


ga_iteration(list_name,maxpsFitness,flag_variable,0,0,flag2,maximum)
