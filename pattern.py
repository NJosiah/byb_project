tracker = 2

for i in range(1,10):
    if i < 6:
        print(i*"*")
    else:
        print((i - tracker)*"*")
        tracker +=2
        