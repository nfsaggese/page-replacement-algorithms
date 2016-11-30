import sys

#print(str(sys.argv[1]))

frames = int(sys.argv[1])

replacements = 0

counter = 0

references = [1,2,3,4,2,1,5,6,2,1,2,3,7,6,3,2,1,2,3,6]
memory = []
print(str(references))
for i in range(0,frames):
	memory.append([-1,-1])#initialize memory representation

for i in references:
	try:
		sub = list(x[0] for x in memory)
		ind = sub.index(i)#index received
		memory[ind][1] = counter
	except Exception as e:
		#doesn't exist
		sub = list(x[1] for x in memory)
		#print(sub)
		minind = sub.index(min(sub))
		#replace
		memory[minind] = [i,counter]
		replacements+=1
	counter+=1


print(replacements)
