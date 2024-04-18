string = input("Enter a random sentence: ")
new_string = "".join([string[i].upper() if i%2==0 else string[i].lower() for i in range(len(string))])
print(new_string)

alternate_string = string.split()
for i in alternate_string:
    print(i.upper())
    





