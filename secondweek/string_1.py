string1="hello,have a good day."
str1="a","e","i","o","u"
for i in string1:
	if i in str1:
		print(i)
# 2
str2="umbrella."
if "e" in str2:
	print("e is present")
#3
str3="refrigerator."
count=0
for i in str3:
	count+=1
print(count)
#4
s4=string1+str2+str3
s5=""
for i in s4:
	if i==".":
		s5+="!"
	else:
		s5+=i
print(s5)
