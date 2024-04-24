

string = input("Enter a random sentence: ")
new_string = "".join([string[i].upper() if i%2==0 else string[i].lower() for i in range(len(string))])
print(new_string)

alternate_string = string.split()
print(alternate_string)

word_list = []
for i in range(len(alternate_string)):
    if i%2==0:
        word_list.append(alternate_string[i].upper())
    else:
        word_list.append(alternate_string[i].lower())

newest_string = " ".join(word_list)
print(newest_string)