#TASK 3
#2)a=[1,2,3,4,5,6,7,8].Find how many odd number and how many even number in the list?



a = 1,2,3,4,5,6,7,8
d1 = 0
d2 = 0
if a[0]%2==0:
    d1 += 1
else:
    d2 += 1
if a[1]%2==0:
    d1 += 1
else:
    d2 += 1
if a[2]%2==0:
    d1 += 1
else:
    d2 += 1
if a[3]%2==0:
    d1 += 1
else:
    d2 += 1
if a[4]%2==0:
    d1 += 1
else:
    d2 += 1
if a[5]%2==0:
    d1 += 1
else:
    d2 += 1
if a[6]%2==0:
    d1 += 1
else:
    d2 += 1
if a[7]%2==0:
    d1 += 1
else:
    d2 += 1
print("The even number in the list are:", d1)
print("The odd number in the list are:", d2)