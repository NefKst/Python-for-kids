# γραμμή 7: ο χρήστης εισάγει έναν δεκαδικό αριθμό (σε μέτρα) και ορίζει μια μεταβλητή x 
# γραμμή 8: η μεταβλητή x πολ/ζεται με το 10 για να μετατραπεί σε δέκατα και το αποτέλεσμα αποθηκεύεται στη μεταβλητή y 
# γραμμή 9: εμφανίζεται η μεταβλητή y (ως κείμενο) και προστίθεται στο τέλος η λέξη "δέκατα"

# με τον ίδιο τρόπο, η μεταβλητή y ορίζεται κάθε φορά εκ νέου και υπολογίζονται χιλιοστά και χιλιόμετρα

x = float(input ("Εισάγετε σε μέτρα την απόσταση που θέλετε να μετατρέψετε:"))
y = float(x * 10)
print (str(y) + " δέκατα")
y = float(x * 100)
print (str(y) + " εκατοστά")
y = float(x * 1000)
print (str(y) + " χιλιοστά")
y = float(x / 1000)
print (str(y) + " χιλιόμετρα")
