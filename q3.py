"""Write a Python program to create a list of tuples with the first element as the
number and Second element as the square of the number.
E.g. list = [3, 9, 10]
Output: [(3, 9), (9, 81), (10, 100)]"""

el=input("enter the element:").split()
list1=[]
for i in el:
    x=int(i)
    list1.append(x)

list2=[]
for e in list1:
    t=(e,e*e)
    list2.append(t)
print("\nList containing (n,n^2) is shown below:")
print(list2)