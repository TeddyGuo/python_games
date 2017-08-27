def prime_det(num):
    if num == 1:
        return 0
    elif num == 2:
        return 1
    for i in range(2,num):
        if (num % i) == 0:
            return 0
        else:
            return 1

line = int(input("How many lines do you have : "))

if line <= 10:
    for i in range(line):
        start = int(input("Start number : "))
        end = int(input("End number : "))
        if start >= 1 and start <= end and end <= 1000000000 and (end - start) <= 100000:
            for j in range(start, end + 1):
                if prime_det(j) == 1:
                    print("%d" % (j))
        else:
            print("error! Please pay attention to the bound of inputs.")
else:
    print("error! Please input a number less or equal to 10 and bigger than 0.")
