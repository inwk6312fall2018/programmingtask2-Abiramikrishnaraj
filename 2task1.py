#Comment
file=open("Crime.csv")
dict={}
dict2={}
l1=[] #list1
l2=[] #list2
for line in file:
	line=line.strip()
	line=line.split(",")
	l1.append(line[-1]) #listing all crime type in l1
	l2.append(line[-2]) #listing all crime id in l2
"""Counting crime name and crime count"""
for i in l1:
		if i not in dict: #crime type-i not in l1
			dict[i]=1 #append the element i
		else:		  #else
			dict[i]+=1 #add count
print(dict)
"""Counting Crime ID"""
for y in l2:
		if y not in dict2: #crime ID not in l2
			dict2[y]=1 #append the element y
		else:		   #else
			dict2[y]+=1 #add the count
#print(dict2)
"""zipping Crime name, crime  ID"""
test=zip(dict,dict2)
for xy in test:
	print(xy)


