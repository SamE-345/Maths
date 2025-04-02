import re

equation = "3x^4"
Subfunctions = []
Subfunctions.append(re.findall("[1-9]*x\^-?[1-9]+", equation))

Subfunctions.append(re.findall("[1-9]*e\^-?[1-9]+x", equation))
Subfunctions.append(re.findall("[1-9]*(sin|cos|tan)\([1-9]*x\^?[1-9]*)"))
Subfunctions.append(re.findall("[1-9]$"))

def Create_Function():
    temp_Array = []
    for i in range(Subfunctions.len):
        pass
        

        
        #temp_Function = lambda x : 
def is_Num(char):
    nums = [0,1,2,3,4,5,6,7,8,9]
    if char in nums:
        return True
    else:
        return False
        
