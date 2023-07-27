from copy import deepcopy
dic1={1:"a",2:" b",3:"c",4:"d"}
dic2={5:"e",6:"f",7:"g",8:"i"}
#print(dic1 | dic2)
#print(dic1,dic2)
print(dic1)
dic3=deepcopy(dic2)
dic3[5]="Hello"
print(dic3)
dic3.update(dic2)
print(dic3)