age = int(input("enter your age"))
if age > 5 and age < 12:
    print("child")
elif age > 12 and age < 18:
    print("teenager")
elif age > 18:
    print("adult")
else:
    print("not in the chart")