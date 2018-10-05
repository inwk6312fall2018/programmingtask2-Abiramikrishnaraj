#Comment
file=open("Crime.csv")
count=Counter()
dict={}
l1=[] #list1
l2=[] #list2
l3=[] #list3
for line in file:
	line=line.strip()
	line=line.split(",")
	l1.append(line[-1]) #listing all crime type in l1
	l2.append(line[-2]) #listing all crime id in l2
for i in l1:
		if i not in dict:
			dict[i]=1
		else:
			dict[i]+=1
print([dict])
#test=zip(dict,l2)
#for xy in test:
#	print(xy)
#print(l2[0:])
		#count[i]+=1
	#print(dict,l2)

