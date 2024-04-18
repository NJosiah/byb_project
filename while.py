listofnums=[]
def average(listofnums):
    return sum(listofnums) / len(listofnums)

listofnums.append()
print(listofnums)
    
num = int(input("Enter a number: "))
listofnums.append(num)
print(listofnums)
while num > 0:
    num = int(input("Enter a number: "))
if num == -1:
    print("the sum is: ", sum(listofnums))
    print("the average is: ", average(listofnums))



