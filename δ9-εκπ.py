x =  int(input("Eισάγετε τον πρώτο αριθμό: "))
y =  int(input("Eισάγετε τον δεύτερο αριθμό: "))

i = 1

if x > y:
    while (x * i) % y != 0:
        i = i + 1
    print("Το ΕΚΠ είναι το: " + str(x * i))

if y > x:
    while (y * i) % x != 0:
        i = i + 1
    print("Το ΕΚΠ είναι το: " + str(y * i))

if x == y:
    print("To ΕΚΠ είναι το: " + str(x))