x =  int(input("Εισάγετε τον πρώτο αριθμό: "))
y =  int(input("Εισάγετε τον δεύτερο αριθμό: "))
z =  int(input("Εισάγετε τον τρίτο αριθμό: "))

if x > y and x > z:
    if y > z:
        print (str (x) + ">" + str(y) + ">" + str(z))
    if y < z:
        print (str (x) + ">" + str(z) + ">" + str(y))

elif y > x and y > z:
    if x > z:
        print (str (y) + ">" + str(x) + ">" + str(z))
    if x < z:
        print (str (y) + ">" + str(z) + ">" + str(x))

else:
    if x > y:
        print (str (z) + ">" + str(x) + ">" + str(y))
    if x < y:
        print (str (z) + ">" + str(y) + ">" + str(x))
