#Write a Python program to square the elements of a list using map() function.
n=input("enter the list using map:")
n=[4,5,2,9]
result=list(map(lambda x:x**2,n))
print(result)