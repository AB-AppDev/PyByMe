"""Literals And Identifiers"""

A = 15

"""
A is variable so called it as IDENTIFIERS
15 is constant aka Literals
'=' Store literal in identifier

15 - Numeric Literal
3.5 - Float Literal
0b01001110 - Binary Literal
OxA12C - Hex Literal
True/False - Bool Literal
"""

B = 15
C = 15

print(id(A))
print(id(B))
print(id(C))
print()
A = 10
print(id(A))
print(id(B))
print(id(C))


"""All identifiers will point to same location"""