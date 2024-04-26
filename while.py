listofnums=[]
def average(listofnums):
    return sum(listofnums) / len(listofnums)
    
num = int(input("Enter a number: "))

while num > 0:
    listofnums.append(num)
    num = int(input("Enter a number: "))
if num == -1:
    print("the sum is: ", sum(listofnums))
    print("the average is: ", average(listofnums))
