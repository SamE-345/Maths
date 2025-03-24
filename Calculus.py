import re

equation = "3x^4 + 5x^2"

Polynomials = re.findall("[1-9]* x \^ -? [1-9]+")
print(Polynomials)

Exponentials = re