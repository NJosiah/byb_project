# Triathlon Awards

swim_time_secs = int(input("How long did they take to swim? "))
swim_time_min, swim_time_secs = divmod(swim_time_secs, 60)
print("%02d:%02d" % (swim_time_min, swim_time_secs))

cycling_time_secs = int(input("How long did they take to cycle? "))
cycling_time_min, cycling_time_secs = divmod(cycling_time_secs, 60)
print("%02d:%02d" % (cycling_time_min, cycling_time_secs))

run_time_secs = int(input("How long did they take to run? "))
run_time_min, run_time_secs = divmod(run_time_secs, 60)
print("%02d:%02d" % (run_time_min, run_time_secs))

total_time_min = int((swim_time_min + cycling_time_min + run_time_min))
print(total_time_min)

if total_time_min <= 100:
    print("Congratulations you have qualified! You are awarded with provincial colours")
elif total_time_min <= 101:
    print("Congratulations you are awarded with provincial half colours!")
elif total_time_min <= 106:
    print("Congratualtions you are awarded with a provincial scroll!")
else:
    print("Unfortnately no award is given")