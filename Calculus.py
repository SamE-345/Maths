import re

equation = "3x^4"

Polynomial = re.findall("[1-9]*x\^-?[1-9]+", equation)
print(Polynomial)
Exponential = re.findall("[1-9]*e\^-?[1-9]+x", equation)
Trig = re.findall("[1-9]*(sin|cos|tan)\([1-9]*x\^?[1-9]*)")
Constants = re.findall("[1-9]$")