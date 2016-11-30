import sys

#print(str(sys.argv[1]))

frames = int(sys.argv[1])

replacements = 0

counter = 0

references = [1,2,3,4,2,1,5,6,2,1,2,3,7,6,3,2,1,2,3,6]
memory = []
print(str(references))
for i in range(0,frames):
	memory.append(-1)#initialize memory representation

for i in references:
	try:
		memory.index(i)
	except Exception as e:
		#wasn't in memory
		temp = memory[:(len(memory)-1)]
		memory = [i]
		memory.extend(temp)#new element in front others attached to rear
		replacements += 1

		

print(replacements)
