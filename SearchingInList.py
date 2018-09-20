list=[10,12,13,24,34,27]
num=int(input("Enter the number to be searched in the list\n"))
print (num)
for item in range(len(list)):
    if list[item]==num:
        print("\n item found")
        print("\n position",list.index(num))
        break
else:
    print("item not found")
