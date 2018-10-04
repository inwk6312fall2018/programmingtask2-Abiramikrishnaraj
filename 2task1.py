#Comment
from collections import Counter
file=open("Crime.csv")
count=Counter()
dict1={}
dict2={}
l1=[] #list1
l2=[] #list2
for line in file:
	line=line.strip()
	line=line.split(",")
	l1.append(line[-1])
	#print(l1)
	for i in l1:
		count[i]+=1
	print(l1,count)
""""	for i in l1:
		if i in l1 and i not in l2:
			l2.append(l1)
			print(list(itertools.accumulate(l2)))
			print(''.join(i))"""











#	print(l1)
#	for i in line:
#	print(line[-1],count)
#	print(line[-1],count)
#	x=set(l1)
#	print(x)
#x=set(l1)
#print(x,i)
		#l1.append(line[-1])
		#print(l1)"""

		#else:
		#	i+=line[-1]
		#	print(line[-1])
