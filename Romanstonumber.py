#sorry for the messy code and the broken english
raw=input()

#initializing some values (idk if it's necessary)
pn=0
cn=0
c=0
count=0
al=[]

#error bool
e=False
sv=""
dsub=False

#the dict
table={
"I":1,
"V":5,
"X":10,
"L":50,
"C":100,
"D":500,
"M":1000,
"i":1000,
"v":5000,
"x":10000,
"l":50000,
"c":100000,
"d":500000,
"m":1000000
}

#static list of the dict
l=['I', 'V', 'X', 'L', 'C', 'D', 'M', 'i', 'v', 'x', 'l', 'c', 'd', 'm']

#Quadruple 1 char error
if "IIII" in raw or "XXXX" in raw or "CCCC" in raw or "MMMM" in raw:
	print("Error: repetition of the 1,10,100,1000 characters 4 or more times")
	e=True

#Double 5 char error
if "VV" in raw or "LL" in raw or "DD" in raw:
	print("Error: repetition of 5,50,500 characters")
	e=True

#shitty solution time
for h in raw:
	
	al.append(h)
	c+=1
	
	if pn == 0:
		pn = h
		count= table[pn]
	else:
		pn=l.index(pn)
		cn=l.index(h)
		
		
		#if pn is bigger than cn it's all good fam and we have to sum. MC --> 1000+100=1100 {CX: C->bigger X ->smaller; also this is the general case}
		if pn>cn:
			count= count+ table[l[cn]]
		#we trust that if there was an error of repetition it would block the loop. MMCCXX --> 1000+1000... {CC: C->equals}
		if pn==cn:
			count= count+ table[l[cn]]
		#if the pn is smaller than the cn that means that we are subtracting (and the mx difference in grades allowed is 2 [10]) {XC: X ->smaller; C->bigger}
		if pn<cn and cn-pn<=2 :
			count+= table[l[cn]]- (2*(table[l[pn]]))
			sv=pn
		
		#Subctr error 					i'm not proud of this
		if pn<cn and cn-pn<=2 and len(al) >= 3 and al[-3] == al[-2]:
			print("Error: subtract only one number at a time")
			e=True
			break
		
		#Items error
		if pn<cn and cn-pn>2:
			print("Error: treat 1,10,100,1000 as separate items")
			e=True
			break
		
		#Double subtraction error
		if pn<cn and cn-pn<=2 and pn==sv:
			e=True
			print("Error: double subtraction")
			dsub=True 
	  
	pn = h
	if dsub ==True:
		break
	
		#debbugging infos
		#print(al)
		#print(count,h)
		#print(count,h,table[l[cn]],table[l[cn]])
		#print(h,raw[((raw.index(h))-2)],raw[((raw.index(h))-1)])

if count != 0 and raw != "" and e==False:
	print(count)	#output in stdout