import numpy as np

a=np.array([1,2,3,4,5,6])
b=np.array([6,5,4,3,2,1])
# Simple Opeartions
subrtact=b-a
addition=a+b
squared=b**2
multiplication=a*b
dotproduct=a@b
dotproduct1=a.dot(b)

# print(a>5)
# print(subrtact)
# print(addition)
# print(squared)
# print(multiplication)
# print(dotproduct)
# print(dotproduct1)
# print(a.sum())
# print(a.min())
# print(a.max())
# print(a.cumsum())


an=np.arange(10).reshape(2,5) 
print(an.sum(axis=1))  # [10 35]
print(an.sum(axis=0))  # [5 7 9 11 13]