#Task-1 :- Area of the circle
r=float(input("enter radius value"))
area_circle=3.14*r*r
print(area_circle)

#Task-2:- extension of the file
filename=input("Input the filename:")
f_extns=filename.split(".")
print("the extension of the file is:"+repr(f_extns[-1]))