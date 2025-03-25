import re

equation = "3x^4 dwehiwhi"
Subfunctions = []
Subfunctions.append(re.findall("[1-9]*x\^-?[1-9]+", equation))

Subfunctions.append(re.findall("[1-9]*e\^-?[1-9]+x", equation))
Subfunctions.append(re.findall("[1-9]*(sin|cos|tan)\([1-9]*x\^?[1-9]*)"))
Subfunctions.append(re.findall("[1-9]$"))

def Create_Function():
    temp_Array = []
    temp_Array.append( ) ## Add functions
