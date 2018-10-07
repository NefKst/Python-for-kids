#λειπει ο σχολιασμος

gefsi = int(input ("Τι γεύση θέλετε; \n Γράψτε 1 για σοκολάτα \n Γράψτε 2 για βανίλια \n Γράψτε 3 για φράουλα \nΕπιλέξτε:"))
varos = float(input("Πόσα γραμμάρια ζυγίζει το παγωτό;\nΑπαντήστε:"))
siropi = str(input('Έχετε σιρόπι; ΝΑΙ ή ΟΧΙ\nΑπαντήστε:'))
amygdalo = str(input('Έχετε αμύγδαλο; ΝΑΙ ή ΟΧΙ\nΑπαντήστε:'))
frouta = str(input('Έχετε φρούτα; ΝΑΙ ή ΟΧΙ\nΑπαντήστε:'))
timi = 0

if gefsi == 1:
    timi = (varos * 1)/100
elif gefsi == 2:
    timi =  (varos * 0.90)/100
elif gefsi == 3:
    timi = (varos * 1.10)/100

if siropi == "ΝΑΙ":
    timi = timi + 0.10
if amygdalo == "ΝΑΙ":
    timi = timi + 0.20
if frouta == "ΝΑΙ":
    timi = timi + 0.50

print("Το παγωτό σου κοστίζει €" + str(timi))
